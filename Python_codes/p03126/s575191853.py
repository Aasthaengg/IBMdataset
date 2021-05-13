n,m = map(int,input().split())
x = [0]*(m+1)
for i in range(n):
    d = list(map(int,input().split()))
    for i in d[1:]:
        x[i] += 1
print(x.count(n))
