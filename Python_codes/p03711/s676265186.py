a=[1,3,5,7,8,10,12]
b=[4,6,9,11]

def hantei(x):
  if x in a:
    return 1
  elif x in b:
    return 2
  else:
    return 3

x,y=map(int,input().split())
print("Yes" if hantei(x)==hantei(y) else "No")
