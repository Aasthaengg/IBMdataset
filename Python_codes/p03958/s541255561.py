n,t = map(int,input().split())
a = list(map(int,input().split()))

ma = max(a)
sa = sum(a)
d = sa - ma

print(max(ma-(d+1),0))