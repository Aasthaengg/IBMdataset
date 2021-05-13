a,b=list(map(int, input().split()))
if a%3!=0 and b%3!=0:
  if (a+b)%3==0:
    print("Possible")
  else:
    print("Impossible")
else:
  print("Possible")