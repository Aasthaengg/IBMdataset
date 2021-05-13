A,B = map(int, input().split())

ans = 0

for i in range(100, 1000):
    S = str(i)
    P = S + S[1] + S[0]
    ans += A <= int(P) <= B

print(ans)