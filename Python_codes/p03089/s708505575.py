n = int(input())
b = list(map(int, input().split()))
ans = []

for i in range(n):
    for j in range(len(b), 0, -1):
        if j == b[j-1]:
            b = b[0:j-1] + b[j:n]
            ans.append(j)
            break

if len(ans) == n:
    ans.reverse()
    for item in ans:
        print(item)
else:
    print(-1)

