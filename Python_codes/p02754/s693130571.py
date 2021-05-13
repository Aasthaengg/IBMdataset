N, A, B = map(int, input().split())

ans = 0

ans += (N//(A+B))*A
ans += min(int(N%(A+B)), A)

print(ans)
