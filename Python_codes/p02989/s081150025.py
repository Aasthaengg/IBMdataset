import sys
input = sys.stdin.readline

N = int(input())
d = list(map(int,input().split()))

sd = sorted(d)
ss = sd[N//2-1]
sb = sd[N//2]
print(sb-ss)
