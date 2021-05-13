n=int(input())
k=0
i=0
while k<n:
    i+=1
    k+=i
print(*[j for j in range(1,i+1) if k-n!=j],sep='\n')