from fractions import Fraction
n,k=map(int,input().split())
times=[0]*n
for i in range(1,n+1):
    count=0
    j=1
    while True:
        if j*i<k:
            count+=1
            j=2*j
        else:
            break
    times[i-1]+=count
ans=0
for k in times:
    ans+=(Fraction(1,2))**k
print(ans.numerator/(ans.denominator*n))