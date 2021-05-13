N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
tim, ans = sum(B), 0
r = M - 1

#Aを1冊も読まないとき
while r > -1 and tim > K:
    tim -= B[r]
    r -= 1
ans = r + 1

#Aを1冊以上読むとき
for l in range(N):
    tim += A[l]
    while r > -1 and tim > K:
        tim -= B[r]
        r -= 1
    if tim > K:
        break
    ans = max(ans, l + r + 2)
print(ans)
