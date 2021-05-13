n=int(input())
a=list(map(int,input().split()))
if sum(a)==0:
  print("Yes")
else:
  t=list(set(a))
  if len(t)==3 and n%3==0:
    if t[0]^t[1]==t[2] and a.count(t[0])==n//3 and a.count(t[1])==n//3:
      print("Yes")
    else:
      print("No")
  elif len(t)==2 and a.count(0)==n//3 and n%3==0:
    print("Yes")
  else:
    print("No")