import os
import sys
from io import BytesIO, IOBase
from sys import stdin
def input():
    return stdin.readline()

def main():
    N, S = map(int,input().split())
    A = list(map(int,input().split()))
    mod = 998244353
    dp = [[0 for j in range(S + 1)] for i in range(N + 1)]
    dp[0][0]=1
    for i in range(1,N+1) : 
        for j in range(S + 1) : 
            if(j==0):
                dp[i][j]=pow(2,i,mod)
            else:
                dp[i][j]+=2*dp[i-1][j]
                dp[i][j]%=mod
                if(j-A[i-1]>=0):
                    dp[i][j]+=dp[i-1][j-A[i-1]]
            dp[i][j]%=mod
    print(dp[N][S]%mod)
    


# fast-io region

BUFSIZE = 8192


class FastIO(IOBase):
    newlines = 0

    def __init__(self, file):
        self._fd = file.fileno()
        self.buffer = BytesIO()
        self.writable = "x" in file.mode or "r" not in file.mode
        self.write = self.buffer.write if self.writable else None

    def read(self):
        while True:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            if not b:
                break
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines = 0
        return self.buffer.read()

    def readline(self):
        while self.newlines == 0:
            b = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
            self.newlines = b.count(b"\n") + (not b)
            ptr = self.buffer.tell()
            self.buffer.seek(0, 2), self.buffer.write(b), self.buffer.seek(ptr)
        self.newlines -= 1
        return self.buffer.readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.buffer.getvalue())
            self.buffer.truncate(0), self.buffer.seek(0)


class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        self.write = lambda s: self.buffer.write(s.encode("ascii"))
        self.read = lambda: self.buffer.read().decode("ascii")
        self.readline = lambda: self.buffer.readline().decode("ascii")


sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)


def input():
    return sys.stdin.readline().rstrip("\r\n")


def write(*args, end="\n"):
    for x in args[:-1]:
        sys.stdout.write(str(x) + " ")
    sys.stdout.write(str(args[-1]))
    sys.stdout.write(end)


def r_array():
    return [int(x) for x in input().split()]


def r_int():
    return int(input())


if __name__ == "__main__":
    main()

