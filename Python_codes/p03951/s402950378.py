N = int(input())
s = input()
t = input()

ans = 2 * N
for i in range(N):
    for j in range(N - i):
        if s[i + j] != t[j]:
            break
    else:
        ans = min(ans, N + i)
print(ans)
