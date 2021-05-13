N = int(input())
A = list(map(int,input().split()))
money = 1000
stock = 0

for i in range(N-1):
  if A[i] < A[i+1]:
    stock = money // A[i]
    money += stock * (A[i+1] - A[i])
    
print(money)