n = int(input())
a = [int(input()) for _ in range(n)]
ans = 0
j = 0
for i in range(n):
    ans+=1
    if i==0:
      j=a[i]
    if j==2:
      print(ans)
      quit()
    j = a[j-1]
print(-1)
