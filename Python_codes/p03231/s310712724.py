import fractions
N,M = map(int,input().split())
S = input()
T = input()
gcd = fractions.gcd(N,M)
x = N // gcd 
y = M // gcd
check = 0
for i in range(gcd):
    if S[i*x] != T[i*y]:
        check = 1
        break
if check == 1:
    ans = -1
else:   
    ans = N * M // gcd
print(ans)

