n,m=map(int, input().split())
table = [0]*m
c = 0
for i in range(n):
    ans = list(map(int, input().split()))
    for j in range(1,len(ans)):
        table[ans[j]-1] += 1
for i in range(m):
    if table[i] == n:
        c += 1
print(c)

