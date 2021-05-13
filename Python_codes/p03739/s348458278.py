
N=int(input())
A=list(map(int, input().split()))
#和の符号が異なる


ans1=0
ans2=0

if A[0]==0:
    a0_1=1
    a0_2=-1
    ans1+=1
    ans2+=1
elif A[0]>1:
    a0_1=A[0]
    a0_2=-1
    ans2+=A[0]+1
else:
    a0_1=1
    a0_2=A[0]
    ans1+=1-A[0]


now1=a0_1
for i in range(1,N):
    if now1*(now1+A[i])<0:
        now1+=A[i]
    else:
        if now1>0:
            add=(-1)*(now1+1)
        else:
            add=(-1)*(now1-1)
        now1+=add
        ans1+=abs(add-A[i])
    #print(now1)

now2=a0_2
for i in range(1,N):
    if now2*(now2+A[i])<0:
        now2+=A[i]
    else:
        if now2>0:
            add=(-1)*(now2+1)
        else:
            add=(-1)*(now2-1)
        now2+=add
        ans2+=abs(add-A[i])
ans=min(ans1, ans2)
print(ans)
#print(ans1, ans2)