N = int(input())
A = list(map(int,input().split()))
#print(N,A)

sort_A = sorted(A,reverse=True)
#print(sort_A)

Alice = 0
Bob = 0
for i in range(N):
  if i % 2 == 0:
    Alice += sort_A[i]
  else:
    Bob += sort_A[i]

print(Alice - Bob)