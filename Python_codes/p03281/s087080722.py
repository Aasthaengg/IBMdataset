n=int(input())

count=0
for N in range(1,n+1,2):
    fact=0
    for i in range(1,N+1):
        if N%i==0:
            fact+=1
    if fact==8:
        count+=1
print(count)
