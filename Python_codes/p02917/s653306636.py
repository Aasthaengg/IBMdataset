N=int(input())
*B,=map(int,input().split())

ans=B[0]+B[-1]
i=0
while i+1<N-1:
    ans+=min(B[i],B[i+1])
    i+=1

print(ans)