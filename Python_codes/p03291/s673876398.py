mod=10**9+7
s=input()
n=len(s)
Sum_A=[0]*(n+1)
Sum_B=[0]*(n+1)
Sum_C=[0]*(n+1)
Sum_q=[0]*(n+1)
for i in range(1, n+1):
    Sum_A[i]=Sum_A[i-1]
    Sum_C[i]=Sum_C[i-1]
    Sum_q[i]=Sum_q[i-1]
    if s[i-1]=='A':
        Sum_A[i]+=1
    elif s[i-1]=='C':
        Sum_C[i]+=1
    elif s[i-1]=='?':
        Sum_q[i]+=1
ans=0
def count(x, q):
    return int(x*pow(3, q, mod)+q*pow(3, (q-1), mod)) if q>0 else int(x*pow(3, q, mod))
for i in range(n):
    if s[i]=='B' or s[i]=='?':
        ans+=count(Sum_A[i], Sum_q[i])*count(Sum_C[n]-Sum_C[i+1], Sum_q[n]-Sum_q[i+1])
        ans%=mod
print(ans)
