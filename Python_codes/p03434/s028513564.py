N = int(input())
A = list(map(int, input().split()))

A.sort(reverse=True)

Alice = 0
Bob = 0
for i in range(N):
  temp = A.pop(0)
  if i % 2 == 0:
    Alice += temp
  else:
    Bob += temp

print(str(Alice - Bob))