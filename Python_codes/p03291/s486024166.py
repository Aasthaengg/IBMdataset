s = input()
n = len(s)
mod = 10**9+7

a = [0]*n
b = [0]*n
c = [0]*n
d = [0]*n

x = 0
y = 0
for i in range(n):
    a[i] = x
    b[i] = y
    if s[i] == 'A':
        x += 1
    elif s[i] == '?':
        y += 1

x = 0
y = 0
for i in range(n-1,-1,-1):
    c[i] = x
    d[i] = y
    if s[i] == 'C':
        x += 1
    elif s[i] == '?':
        y += 1

def f(A,B,C,D):
    if B+D == 0:
        return pow(3,B+D,mod)*A*C%mod
    if B+D == 1:
        return pow(3,B+D,mod)*A*C%mod + pow(3,B+D-1,mod)*B*C%mod + pow(3,B+D-1,mod)*A*D%mod

    return pow(3,B+D,mod)*A*C%mod + pow(3,B+D-1,mod)*B*C%mod + pow(3,B+D-1,mod)*A*D%mod + pow(3,B+D-2,mod)*B*D%mod

res = 0
for i in range(1,n-1):
    if s[i] == 'B' or s[i]=='?':
        res = (res+f(a[i],b[i],c[i],d[i]))%mod
print(res%mod)