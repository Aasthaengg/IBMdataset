N = int(input())
a = list(map(int, input().split()))

a.sort()

a_1 = []
for i in range(N,3*N):
  a_1.append(a[i])

P = []
for i in range(2*N):
  if i%2 == 0:
    P.append(a_1[i])
    
print(sum(P))