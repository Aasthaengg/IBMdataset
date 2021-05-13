N, K = map(int, input().split())

i = N // K
N = N - K * i
A = N
B = -(A-K)
ans = min(A,B)

print(ans)