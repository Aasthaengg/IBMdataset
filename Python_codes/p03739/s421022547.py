n=int(input())
A=[int(i) for i in input().split()]

pa=0
s=A[0]
if A[0]<=0:
    pa=1-A[0]
    s=1

for i in range(1,n):
    if i%2==1:
        if s+A[i]>=0:
            pa+=s+A[i]-(-1)
            s=-1
        else:
            s+=A[i]
    else:
        if s+A[i]<=0:
            pa+=1-(s+A[i])
            s=1
        else:
            s+=A[i]
ma=0
s=A[0]
if A[0]>=0:
    ma=A[0]-(-1)
    s=-1

for i in range(1,n):
    if i%2==1:
        if s+A[i]<=0:
            ma+=1-(s+A[i])
            s=1
        else:
            s+=A[i]
    else:
        if s+A[i]>=0:
            ma+=s+A[i]-(-1)
            s=-1
        else:
            s+=A[i]
       
print(min(pa,ma))