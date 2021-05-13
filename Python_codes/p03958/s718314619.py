import sys
input = sys.stdin.readline

K,T = list(map(int,input().split()))
a = sorted(list(map(int,input().split())))
amax = a[-1]
asub = sum(a[0:-1])

print(max(0,amax-1-asub))
