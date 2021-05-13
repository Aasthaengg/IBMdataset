n = int(input())
ans = [[0 for i in range(3)] for i in range(n)]

for i in range(3):
    for j in input().split():
        for k, l in enumerate(j):
            ans[k][i] = l
a = 0
for i in ans:
    a += len(set(i))-1
print(a)
