n=int(input())
h=list(map(int,input().split()))
cnt=h[0]
for i in range(1,n):
  if h[i-1] >= h[i]:
    continue
  else:
    cnt += h[i]-h[i-1]
print(cnt)