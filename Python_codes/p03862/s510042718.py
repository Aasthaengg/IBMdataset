N,x = map(int,input().split())
a = [0] + list(map(int,input().split()))
b = [0]
for i in range(1,N):
  b.append(a[i]+a[i+1])

cnt = 0  
for i in range(1,N):
  if b[i] > x:
    c = b[i] - x
    if a[i+1] >= c:
      cnt += c
      if i+1 <= N-1:
        b[i+1] -= c
    else:
      if i+1 <= N-1:
        b[i+1] -= a[i+1]
      cnt += c
print(cnt)    