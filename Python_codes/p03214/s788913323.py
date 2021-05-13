n = int(input())
A = list(map(int, input().split()))
m = sum(A)
l = [ abs(i*n-m) for i in A ]
q = min(l)
for i in range(n):
  if l[i] == q:
    print(i)
    break