N = int(input())
A = list(map(int,input().split()))
A.append(0)

money = 1000
kabu = 0

for i in range(N):
    if kabu > 0:
        money += kabu*A[i]
        kabu = 0
    if A[i] < A[i+1]:
        kabu = money//A[i]
        money -= (money//A[i])*A[i]

print(money)