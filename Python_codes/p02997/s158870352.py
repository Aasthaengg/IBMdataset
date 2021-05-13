n,k = map(int,input().split())

def ans(n,k):  
  ans = (n-1) + ((n-1)*(n-2)//2 - k)
  print(ans)
  c = 0
  for i in range(n):
    for j in range(i+1,n):
      if c >= ans:
        return 
      print(i+1,j+1)
      c += 1

if k > (n-1)*(n-2)//2:
  print(-1)
else:  
  ans(n,k)