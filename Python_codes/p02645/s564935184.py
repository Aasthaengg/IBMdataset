#dt = {} for i in x: dt[i] = dt.get(i,0)+1
import sys
input = sys.stdin.readline
ipnl = lambda n: [int(input()) for _ in range(n)]
inp = lambda :int(input())
ip = lambda :[int(w) for w in input().split()]

s = input()
print(s[:3])