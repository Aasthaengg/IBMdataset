N = int(input())
A = list(map(lambda a: int(a), input().split(" ")))
A.sort(reverse=True)
Alice = []
Bob = []

for i in range(N):
  if i % 2 == 0:
    Alice.append(A[i])
  else:
    Bob.append(A[i])

print(sum(Alice) - sum(Bob))