k,a,b = map(int,input().split())
if a+2>=b:
  print(1+k)
else:
  #bisできるセット
  q = (k-a+1)//2
  if q ==0:
    print(1+k)
  else:
    print(1+(k-2*q)+q*(b-a))