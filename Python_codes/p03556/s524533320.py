n=int(input())
ans=1
for i in range(1,n+2):
  if i**2 > n:
    print(ans**2)
    break
  ans = i