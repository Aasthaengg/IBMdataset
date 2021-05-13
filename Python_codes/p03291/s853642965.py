S=input()
N = len(S)
A = [0]*N
C = [0]*N
L = [0]*N
R = [0]*N
for i in range(1,N):
    A[i] = A[i-1] + (S[i-1] == "A")
    L[i] = L[i-1] + (S[i-1] == "?")
    C[N-1-i] = C[N-i] + (S[N-i] == "C")
    R[N-1-i] = R[N-i] + (S[N-i] == "?")
mod = 10**9+7
d={0:1}
def pow_mod(x,n):
    if d.get(n,False) :return d[n]
    if n<0: return pow_mod(x,mod-1+n)
    if n%2  :
        d[n] = (x*pow_mod(x,n-1))%mod
    else:
        d[n] = (pow_mod(x,n//2)**2)%mod
    return d[n]
ans = 0
for i in range(1,N-1):
    if S[i] in "B?":
        ans += (3*A[i]+L[i])*(3*C[i]+R[i])*pow_mod(3,L[i]+R[i]-2)
        ans %= mod
print(ans)