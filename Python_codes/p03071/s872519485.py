A,B=map(int,input().split())
coin=0
for _ in range(2):
  if A>B:
    coin+=A
    A-=1
  else:
    coin+=B
    B-=1
print(coin)