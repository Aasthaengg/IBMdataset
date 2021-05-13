N = int(input())
S = input()
T = input()

ans = 2 * N
for i in range(1, N + 1):
    if S[-i:] == T[:i]:
        ans = 2 * N - i
print(ans)
