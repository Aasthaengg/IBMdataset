from collections import Counter
H,W=map(int, input().split())
A="".join(input() for _ in range(H))
C=Counter(A)
R=[0]*5
for v in C.values():
    R[4]+=v//4
    v-=v//4*4
    R[2]+=v//2
    v-=v//2*2
    R[1]+=v
R[4]-=(H//2)*(W//2)
x2=(H&1)*(W//2)+(W&1)*(H//2)
if R[4]>=0:
    R[2]+=R[4]*2
    R[4]=0
R[2]-=x2
b=R[4]==0 and R[2]==0 and R[1]==(H&1 and W&1)
print("YNeos"[not b::2])