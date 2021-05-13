N, M = map(int, input().split())
k = [0] * M
s = [0] * M
for i in range(M):
    s[i] = list(map(int, input().split()))
    k[i] = s[i].pop(0)
p = list(map(int, input().split()))

ans = 0

for i in range(2**N):
    b = format(i, "0" + str(N) + "b")
    for j in range(M):
        if sum([int(b[x-1]) for x in s[j]]) % 2 != p[j]:
            break
        if j == M - 1:
            ans += 1

print(ans)