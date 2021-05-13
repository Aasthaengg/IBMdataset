N = int(input())
H = list(map(int, input().split()))
ans = 0
L = 0
count = 0
for i in range(N):
    if L >= H[i]:
        count += 1
    else:
        ans = max(ans, count)
        count = 0
    L = H[i]
ans = max(ans, count)
print(ans)
