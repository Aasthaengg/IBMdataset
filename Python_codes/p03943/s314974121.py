s = list(map(int, input().split()))
if(sum(s)%2==1):
  print("No")
else:
  if(max(s) == (sum(s)//2)):
    print("Yes")
  else:
    print("No")
