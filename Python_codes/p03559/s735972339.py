import bisect
N=int(input())
A=sorted(list(map(int, input().split())))
B=sorted(list(map(int, input().split())))
C=sorted(list(map(int, input().split())))
#真ん中を固定
ba=0
bc=N
ans=0
for i in range(N):
    b=B[i]
    if ba!=N:
        while A[ba]<b:
            ba+=1
            if ba==N:
                break
    if bc!=0:
        while C[N-bc]<=b:
            bc-=1
            if bc==0:
                break
    ans+=ba*(bc)
    #print(ba,bc)
print(ans)
