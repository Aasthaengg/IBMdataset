N = int(input())
A = list(map(int,input().split()))
r = [0]*(N+1)
#累積和
a = 0
for i in range(N):
  a += A[i]
  r[i+1] = a
minimum = 10**18
for i in range(1,N):
  snuke = r[i]
  arai = r[N]-r[i]
  if minimum > abs(snuke-arai):
    minimum = abs(snuke-arai)
print(minimum)