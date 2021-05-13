k,a,b = map(int,input().split())
if b <= a+1:
  print(1+k)  
else:
  if k <= a:
    print(1+k)
  else:   
    ans = (k-a+1)//2*(b-a) + (k-a+1)%2 + a
    print(ans)    