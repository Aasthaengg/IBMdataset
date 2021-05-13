K = int(input())
S = len(input())
P = 10**9+7
nn = 2*10**6+1
fa = [1] * (nn+1)
fainv = [1] * (nn+1)
for i in range(nn):
    fa[i+1] = fa[i] * (i+1) % P
fainv[-1] = pow(fa[-1], P-2, P)
for i in range(nn)[::-1]:
    fainv[i] = fainv[i+1] * (i+1) % P
 
C = lambda a, b: fa[a] * fainv[b] % P * fainv[a-b] % P if 0 <= b <= a else 0

inv = [1]*27
for i in range(2,27):
  inv[i]=(-(P//i)*inv[P%i])%P
ans = 0
a = 1
b = pow(26,K,P)
for i in range(K+1):
  ans = (ans + (C(i+S-1,S-1)*a%P*b%P))%P
  a = a*25%P
  b = b*inv[26]%P
print(ans)