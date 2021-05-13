#from bisect import bisect_left as bl                #c++ lowerbound bl(array,element)
#from bisect import bisect_right as br               #c++ upperbound br(array,element)
#from __future__ import print_function, division    #while using python2
# from itertools import accumulate
# from collections import defaultdict, Counter

def modinv(n,p):
    return pow(n,p-2,p)

def main():
    #sys.stdin = open('input.txt', 'r')
    # sys.stdout = open('output.txt', 'w')

    n, x, m = [int(x) for x in input().split()]
    series = []
    prev = set()
    repeat = []
    ans = 0
    y = x
    repeat_key = -1
    while True:
        if y not in prev:
            prev.add(y)
            series.append(y)
            y = (y * y) % m
        else:
            break

    repeat_key = y
    while True:
        repeat.append(y)
        y = (y * y) % m
        if y == repeat_key:
            break
    # print(series)
    # print(repeat)

    if n <= len(series):
        print(sum(series[:n]))
    else:
        n -= len(series)
        s1 = sum(series)
        s2 = sum(repeat) * (n//len(repeat))

        n %= len(repeat)
        print(s1 + s2 + sum(repeat[:n]))



#------------------ Python 2 and 3 footer by Pajenegod and c1729-----------------------------------------
py2 = round(0.5)
if py2:
    from future_builtins import ascii, filter, hex, map, oct, zip
    range = xrange

import os, sys
from io import IOBase, BytesIO

BUFSIZE = 8192
class FastIO(BytesIO):
    newlines = 0
    def __init__(self, file):
        self._file = file
        self._fd = file.fileno()
        self.writable = "x" in file.mode or "w" in file.mode
        self.write = super(FastIO, self).write if self.writable else None

    def _fill(self):
        s = os.read(self._fd, max(os.fstat(self._fd).st_size, BUFSIZE))
        self.seek((self.tell(), self.seek(0,2), super(FastIO, self).write(s))[0])
        return s
    def read(self):
        while self._fill(): pass
        return super(FastIO,self).read()

    def readline(self):
        while self.newlines == 0:
            s = self._fill(); self.newlines = s.count(b"\n") + (not s)
        self.newlines -= 1
        return super(FastIO, self).readline()

    def flush(self):
        if self.writable:
            os.write(self._fd, self.getvalue())
            self.truncate(0), self.seek(0)

class IOWrapper(IOBase):
    def __init__(self, file):
        self.buffer = FastIO(file)
        self.flush = self.buffer.flush
        self.writable = self.buffer.writable
        if py2:
            self.write = self.buffer.write
            self.read = self.buffer.read
            self.readline = self.buffer.readline
        else:
            self.write = lambda s:self.buffer.write(s.encode('ascii'))
            self.read = lambda:self.buffer.read().decode('ascii')
            self.readline = lambda:self.buffer.readline().decode('ascii')

sys.stdin, sys.stdout = IOWrapper(sys.stdin), IOWrapper(sys.stdout)
input = lambda: sys.stdin.readline().rstrip('\r\n')

if __name__ == '__main__':
   main()
