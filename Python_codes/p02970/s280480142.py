N, D = map(int, input().split())
ans = 0
i = D+1

while True:
    ans += 1
    if D+i >= N:
        break
    i += 2*D + 1

print(ans)