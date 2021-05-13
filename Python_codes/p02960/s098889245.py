import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
from copy import copy 
def main():
    S = readline().decode().rstrip()    
    P = int(1e9)+7
    dp = [0 for _ in range(13)]
    dp[0] = 1
    mul = 1
    for s in reversed(S):
        nxDP = [0 for _ in range(13)]
        if s == '?':
            for i in range(10):
                for j in range(13):
                    nxr = (i*mul+j)%13
                    nxDP[nxr] += dp[j]
                    nxDP[nxr] %= P
        else:
            for j in range(13):
                nxr = ((ord(s)-ord('0'))*mul+j)%13
                nxDP[nxr] += dp[j]
                nxDP[nxr] %= P
        dp = copy(nxDP)
        mul *= 10
        mul %= 13

    print(dp[5])
if __name__ == '__main__':
    main()