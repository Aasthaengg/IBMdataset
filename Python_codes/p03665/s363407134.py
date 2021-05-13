from math import factorial
def cmb(a,b):
    return factorial(a)//factorial(b)//factorial(a-b)
N,P = map(int,input().split())
A = list(map(int,input().split()))
Odd = 0 
Even = 0
for Ai in A:
    if Ai % 2 == 0:
        Even += 1
    else:
        Odd += 1
ans = 0
if P == 0:
    for i in range(Odd+1)[::2]:
        ans += cmb(Odd,i)
else:
    for i in range(Odd+1)[1::2]:
        ans += cmb(Odd,i)
ans *= pow(2,Even)
print(ans)