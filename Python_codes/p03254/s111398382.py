N,x=map(int, input().split())
A=list(map(int, input().split()))

ans=0
A=sorted(A)
for i in range(N):
    a=A[i]
    if x>=a:
        x-=a
        ans+=1
    else:
        i-=1
        break

if x>0 and i==N-1:
    ans-=1
print(ans)