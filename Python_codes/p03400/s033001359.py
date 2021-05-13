n = int(input())
d,x = map(int, input().split())
A = [int(input()) for i in range(n)]

L = []
for i in range(len(A)):
  a = d // A[i]
  if (a*A[i])+1 <= d:
    L.append(a+1)
  else:
    L.append(a)
print(sum(L) + x)