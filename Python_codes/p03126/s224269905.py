n,m = map(int,input().split())
like = set(range(1,m+1))
for _ in range(n):
    a = list(map(int,input().split()))
    like = like & set(a[1:])

print(len(like))