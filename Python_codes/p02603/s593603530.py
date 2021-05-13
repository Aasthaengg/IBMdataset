N = int(input())
A = list(int(a) for a in input().split())
A.extend([0])

money = 1000
stock = 0

for i in range(N):
    if A[i] < A[i+1] and money >= A[i]:
        stock += money // A[i]
        money %= A[i]
    if A[i] > A[i+1]:
        money += stock * A[i]
        stock = 0

print(money)