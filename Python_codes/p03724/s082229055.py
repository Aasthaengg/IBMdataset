n,m = map(int,input().split())
lst = [0]*(n+1)
for _ in range(m):
    a,b = map(int,input().split())
    lst[a] += 1
    lst[b] += 1
res = True
for i in range(1, n+1):
    if lst[i]%2!=0:
        res=False
        break
print('YES' if res else 'NO')