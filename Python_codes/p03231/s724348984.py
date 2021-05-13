from fractions import gcd
N,M = map(int,input().split())
s = input()
t = input()
n = N//gcd(N,M)
m = M//gcd(N,M)
for i in range(gcd(N,M)):
    if s[i*n] == t[i*m]:
        continue
    else:
        print(-1)
        break
else:
    print(N*M//gcd(N,M))
                
