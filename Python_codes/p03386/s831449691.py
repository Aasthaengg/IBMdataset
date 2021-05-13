A,B,K=map(int,input().split())
List=[]
for i in range(K):
  if A<= A+i <= B:
    List.append(A+i)
  if A<= B-i <= B:
    List.append(B-i)
s_l=set(List)
NewList=list(s_l)
NewList.sort()
for i in NewList:
  print(i)