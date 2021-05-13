def hanntei(x):
  a=[1,3,5,7,8,10,12]
  b=[4,6,9,11]
  c=[2]
  if x in a:
    return "a"
  elif x in b:
    return "b"
  else:
    return "c"
x,y=map(int,input().split())
x=hanntei(x)
y=hanntei(y)
print("Yes" if x==y else "No")