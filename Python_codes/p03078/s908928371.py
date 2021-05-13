X,Y,Z,K=map(int,input().split())
A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=list(map(int,input().split()))
A.sort(reverse=True)
B.sort(reverse=True)
C.sort(reverse=True)
list1=[]
for i in range(X):
  for j in range(Y):
      list1.append(A[i]+B[j])
list1.sort(reverse=True)
list1=list1[:K+1]
list2=[]
for i in range(min(X*Y,K)):
  for j in range(Z):
    list2.append(list1[i]+C[j])
list2.sort(reverse=True)
for i in range(K):
  print(list2[i])
