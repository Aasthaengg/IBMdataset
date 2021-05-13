A=input()
N=len(A)
#全組み合わせの中から回文であるものを引く
sm=(N*(N-1))//2
sm+=1

x=dict()
for i in range(N):
    s=A[i]
    if s in x:
        x[s]+=1
    else:
        x[s]=1

val=0
for idx in x:
    v=x[idx]
    val+=(v*(v-1))//2

ans=sm-val
print(ans)