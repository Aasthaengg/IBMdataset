from math import log2,ceil
n,k=[int(s) for s in input().split()]

sum=0
for t in range(1,n+1):
    if t>=k:
        sum+=1
    else:
        sum+=1/(2**ceil(log2(k/t)))
print(sum/n)