N = int(input())
K = int(input())

i = 0
ans = 1
while True:
    if i == N:
        break
    if ans < K:
        ans *= 2
        i += 1
    else:
        ans += K
        i += 1

print(ans)