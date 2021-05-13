N = int(input())
a = list(map(int, input().split()))
n = max(a)
r = 0
for i in range(N):
  if(abs(a[i] -  (n/2)) < abs(r -  (n/2))):
    r = a[i]
print(n, r)