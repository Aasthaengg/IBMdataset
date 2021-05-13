N = int(input())

Order = []

for i in range(N+1):
    Order.append(0)

A = list(map(int, input().split()))

for n in range(N):
    i = A[n]
    Order[i] = n + 1

ans = ""

for i in range(1, N+1):
    ans += str(Order[i])
    if i != N + 1:
        ans += " "

print(ans)