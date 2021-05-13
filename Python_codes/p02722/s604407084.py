n=int(input())

cnt=0
import math

result=set([])

for i in range(1,int(math.sqrt(n-1))+1):
    if (n-1)%i==0:
        for item in [i,(n-1)//i]:
            if item!=1:result.add(item)

for i in range(1,int(math.sqrt(n))+1):
    if n%i==0:
        for item in [i,n//i]:
            if item!=1:
                N=n
                while N%item==0:N=N//item
                if N==1:result.add(item)
                elif N%item==1:result.add(item)

print(len(result))

        
