Moji=str(input())
ListNAB=Moji.split() #N,A,Bの順にリストに格納
N=int(ListNAB[0])
A=int(ListNAB[1])
B=int(ListNAB[2])
if A>=B:
  nmax=B

elif A<B:
  nmax=A

if N>A+B:
  nmin=0

if N<=(A+B):
    nmin=A+B-N

print(str(nmax)+" "+str(nmin))
