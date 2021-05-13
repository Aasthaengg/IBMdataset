N = int(input())
D, X = map(int, input().split())
A = [int(input()) for _ in range(N)]
ans = 0
for i in A:
    for j in range(101):
        if (j * i) + 1 > D:
            ans += j
            break
print(ans + X)
