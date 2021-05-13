N=int(input())
data=[]
for i in range(N):
  S,P=input().split()
  P=int(P)
  data.append((S,-P,i+1))
data.sort()
for _,_,i in data:
  print(i)
