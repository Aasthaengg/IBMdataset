n=int(input())
a=list(map(int,input().split()))
mina=32
for aa in a:
  for i in range(31):
    if aa % (2**i) !=0:
      mina=min(mina,i-1)
print(mina)