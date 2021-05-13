x,y=map(int,input().split())
gift=[x]
x=2*x
while x<=y:
  gift.append(x)
  x*=2
print(len(gift))