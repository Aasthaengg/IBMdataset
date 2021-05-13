N=int(input())
A=[]
for i in range(N):
    a=int(input())
    A.append(a)

if A[0]!=0:
    print(-1)
    exit()

cur=0
ans=0
for a in A:
    if a<=cur:
        ans+=a
    elif a==(cur+1):
        ans+=1
    else:
        print(-1)
        exit()
    cur=a

print(ans)
