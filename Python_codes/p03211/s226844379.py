mina=100000000
N=int(input())
L=list(map(int,list(str(N))))
for i in range(len(L)-2):
  c=L[i]*100+L[i+1]*10+L[i+2]
  mina=min(abs(c-753),mina)
print(mina)