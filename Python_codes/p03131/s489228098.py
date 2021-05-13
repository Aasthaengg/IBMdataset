k,a,b=map(int,input().split())
if b-a <= 2:
  print(k+1)
  exit()
if k-a<1:
  print(k+1)
  exit()
print(1 + (a-1) + (b-a)*((k-(a-1))//2) + (k-(a-1))%2)