n,k=map(int,input().split())

numk=k
for _ in range(2,n+1):
    numk=numk*(k-1)
print(numk)