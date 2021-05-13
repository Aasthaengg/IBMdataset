import sys
import collections

read=sys.stdin.buffer.read
readline=sys.stdin.buffer.readline
readlines=sys.stdin.buffer.readlines

N=int(readline())
A=collections.Counter(read().splitlines())

print(len([v for k,v in A.items() if v%2==1]))