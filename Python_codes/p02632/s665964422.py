#def nCr(n,r):
#    return fact[n]*(inv[n-r]%M)*(inv[r]%M)
M = 1000000007
k = int(input())
s = len(input())
t = k+s
fact = [1]
p25 = [1]
for i in range(1,t+1):
    fact += [(fact[-1] * i)%M]
    if i<=k:
        p25  += [(p25[-1] * 25) % M]

inv = [1]*(t+1)
inv[t] = pow(fact[t], M-2, M)
for i in range(t-1, -1, -1):
    inv[i] = inv[i+1] * (i+1) % M

M = 1000000007
def nCr(n, r, M):
    return fact[n] * inv[n-r] % M * inv[r] % M

n = t#int(input('Enter a number n for checking all its nCr - '))

fact = [1] * (n + 1)
inv = [1] * (n + 1)

for i in range(1, n + 1):
    fact[i] = fact[i-1] * i % M

inv[n] = pow(fact[n], M - 2, M)
for i in range(n-1, -1, -1):
    inv[i] = inv[i + 1] * (i + 1) % M


res = 0
for i in range(k+1):
    #print(nCr(t,t-i))
    res+=nCr(t,t-i,M)*p25[i]
    #print(res)
    res%=M
    #print(res)
print(res)