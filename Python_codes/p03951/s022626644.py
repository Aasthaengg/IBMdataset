# 3:25
N = int(input())
S = input()
T = input()

ans = 2 * N
for i in range(N, 0, -1):
    if S[-i:] == T[:i]:
        ans = 2 * N - i
        break
print(ans)
