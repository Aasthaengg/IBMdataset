n = int(input())
ans = []
for i in range(1, n):
    for j in range(i+1, n+1):
        if i+j==n//2*2+1:
            continue
        ans.append((i, j))
print(len(ans))
for i in ans:
    print(*i)