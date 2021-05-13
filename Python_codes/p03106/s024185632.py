A,B,K=list(map(int,input().split()))

ans=[]
for i in range(1,101):
  if A%i ==0 and B%i==0:
    ans.append(i)
A=ans[::-1]
print(A[K-1])