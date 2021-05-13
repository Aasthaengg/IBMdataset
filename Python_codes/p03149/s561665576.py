a,b,c,d = map(int,input().split())
 
li = [1,9,7,4]
 
if (a in li)and (b in li)and(c in li)and(d in li):
  if a!=b and b!=c and c!=d and a!=c and a!=d and b!=d:
	  print("YES")
  else:
    print("NO")
else:
  print("NO")