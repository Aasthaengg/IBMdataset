x,k,d=map(int,input().split())
x=abs(x)
first_move=x//d
if first_move>k:
  x-=k*d
  x=abs(x)
  print(x)
  exit()

x-=first_move*d
x=abs(x)
k-=first_move
print(abs(x-d) if k&1 else x)