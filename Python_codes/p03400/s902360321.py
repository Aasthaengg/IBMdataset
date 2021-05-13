N = int(input())
D, X = map(int, input().split())
ans = X
for i in range(N):
    a = int(input())
    for j in range(0, 101):
        if j * a + 1 <= D:
            ans += 1
print(ans)
