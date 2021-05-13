n,m,k,j = list(map(int,input().split()))

if (abs(m-n)<=j and abs(k-m)<=j) or abs(k-n)<=j:
  print("Yes")
else:
  print("No")