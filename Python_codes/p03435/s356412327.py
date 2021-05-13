[(a,b,c),(d,e,f),(g,h,i)] = [map(int,input().split()) for i in range(3)]

if a-b==d-e==g-h and b-c==e-f==h-i:
  print("Yes")
else:
  print("No")
