n = int(input())
l = [list(input()) for _ in range(3)]

x=[[] for _ in range(n)]
for i in range(3):
    for j in range(n):
        x[j].append(l[i][j])

ans=0
for i in x:
    ans += len(set(i)) - 1

print(ans)