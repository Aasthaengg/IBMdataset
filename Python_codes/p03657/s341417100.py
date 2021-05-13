a,b=map(int,input().split())
ans=[a%3,b%3,(a+b)%3]
if 0 in ans:
  print("Possible")
else:
  print("Impossible")