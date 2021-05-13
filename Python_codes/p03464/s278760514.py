n=int(input())
arr=list(map(int,input().split()))
arr=arr[::-1]
if arr[0]!=2:
  print(-1)
else:
  arr=arr[1:]
  l=2
  r=3
  for val in arr:
    if (l<=val*(l//val)<=r) or (l<=val*(r//val)<=r):
      if l%val!=0:
        l=val*(l//val+1)
      r=val*(r//val+1)-1
    else:
      print(-1)
      break
  else:
    print(l,r)