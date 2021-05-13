N = int(input())
h = list(map(int,input().split()))
a = [0]*N
ans = 0
for i in range(N):
  while a[i]<h[i]:
    ans += 1
    for j in range(i,N):
      if a[j]==h[j]:
        break
      a[j] += 1
print(ans)