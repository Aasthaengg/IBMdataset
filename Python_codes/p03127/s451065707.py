N=int(input())
*A,=map(int,input().split())
A.sort()

ans=A[0]
count=[0]*N
i=0
while i<N:
    count[i]=A[i]%ans
    i+=1

for c in count:
    if c>0:
        ans=min(ans,c)

for a in A:
    if a%ans>0:
        ans=min(ans,a%ans)

for a in A:
    if a%ans>0:
        ans=min(ans,a%ans)

for a in A:
    if a%ans>0:
        ans=min(ans,a%ans)

for a in A:
    if a%ans>0:
        ans=min(ans,a%ans)

for a in A:
    if a%ans>0:
        ans=min(ans,a%ans)

for a in A:
    if a%ans>0:
        ans=min(ans,a%ans)

for a in A:
    if a%ans>0:
        ans=min(ans,a%ans)

for a in A:
    if a%ans>0:
        ans=min(ans,a%ans)

for a in A:
    if a%ans>0:
        ans=min(ans,a%ans)

print(ans)