p = 10**9+7
def pow(x,m):
    if m==0:
        return 1
    if m==1:
        return x
    if m%2==0:
        return (pow(x,m//2)**2)%p
    else:
        return (x*pow(x,(m-1)//2)**2)%p
L = input().strip()
N = len(L)
C = [0 for _ in range(N)]
for i in range(1,N):
    if L[i-1]=="1":
        C[i] = C[i-1]+1
    else:
        C[i] = C[i-1]
tot = 0
for i in range(N):
    if L[i]=="1":
        tot = (tot+pow(3,N-1-i)*pow(2,C[i]))%p
if L[N-1]=="0":
    tot = (tot+pow(2,C[N-1]))%p
else:
    tot = (tot+pow(2,C[N-1]+1))%p
print(tot)