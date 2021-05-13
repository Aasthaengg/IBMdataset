N = int(input())
A = [int(i) for i in input().split()]
avg = sum(A) / len(A)
l = []
for i in range(N):
  l.append(abs(A[i]-avg))
c = min(l)
print(l.index(c))