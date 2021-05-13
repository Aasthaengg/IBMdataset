def isok(a):
    for j in range(21):
        if(a>>j&1):
            if(bit[j]>0):
                return False
    return True
def bitplus(a):
    for j in range(21):
        if(a>>j&1):
            bit[j]+=1
def bitdif(a):
    for j in range(21):
        if(a>>j&1):
            bit[j]-=a>>j&1

N=int(input())
A=list(map(int,input().split()))
left=0
ans=0
bit=[0]*21
right=0
while(left<N):
    while(right<N and isok(A[right])):
        bitplus(A[right])
        right+=1
    ans+=right-left
    if right==left:
        right+=1
    else:
        bitdif(A[left])
    left+=1
print(ans)