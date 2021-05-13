import sys,collections
input = sys.stdin.readline
m=10**9+7

N=int(input())
S=input().rstrip()
Sc = collections.Counter(S)
cnt = 1
for s in Sc.values():
    cnt *= (s+1)
print((cnt-1)%m)
