A = list(map(int, input().split()))
A.sort()
g=0
k=0
cnt=0
for i in A:
    if i%2==0:
        g+=1
if g==0 or g==3:
    cnt=(2*A[2]-A[0]-A[1])/2
elif g==1:
    for i in range(3):
        if A[i]%2==1:
            A[i]+=1
    cnt=(2*A[2]-A[0]-A[1])/2+1
elif g==2:
    for i in range(3):
        if A[i]%2==0:
            A[i]+=1
    cnt=(2*A[2]-A[0]-A[1])/2+1
    
print(int(cnt))
