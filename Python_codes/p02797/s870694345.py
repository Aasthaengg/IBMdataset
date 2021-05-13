n,k,s = map(int,input().split())
tmp = s+11 if s<10**9 else s-11
li = [s]*k + [(tmp)]*(n-k)
print(*li)