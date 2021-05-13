A,B,K=map(int,input().split())
check=list()
for i in range(1,min(A,B)+1):
  if A%i==B%i==0:
    check.append(i)
print(check[-K])
