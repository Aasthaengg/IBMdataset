N=int(input())
P=[]
for _ in range(N):
  P.append(int(input()))
P.sort()
P[-1]//=2
print(sum(P))