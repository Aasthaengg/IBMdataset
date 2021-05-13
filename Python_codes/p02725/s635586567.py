K,N = map(int,input().split())
a = list(map(int,input().split()))
b = K - a[N - 1] + a[0]
d = 10**20
for i in range(N):
  if i == 0:
    if b < a[i + 1] - a[i]:
      c = K - (a[i + 1] - a[i])
    else:
      c = K - b
  if i == N - 1:
    if a[i] - a [i - 1] < b:
      c = K - b
    else:
      c = K - (a[i] - a[i - 1])
  else:
    if a[i] - a[i - 1] < a[i + 1] - a[i]:
      c = K - (a[i + 1] - a[i])
    if a[i] - a[i - 1] < a[i + 1] - a[i]:
      c = K - (a[i + 1] - a[i])
  if d > c:
    d = c
print(d)