N = int(input())
A = list(map(int,input().split()))

money = 1000
stocks = 0

for n in range(N-1):
  if A[n] < A[n+1]:
    stocks += money//A[n]
    money = money%A[n]
  elif A[n] > A[n+1]:
    money += stocks*A[n]
    stocks = 0
money += stocks * A[-1]
print(money)
