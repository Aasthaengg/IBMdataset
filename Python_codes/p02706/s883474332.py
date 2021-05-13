#ABC163B
n,m = map(int,input().split())
a = list(map(int,input().split()))
print(-1 if sum(a) > n else n-sum(a))