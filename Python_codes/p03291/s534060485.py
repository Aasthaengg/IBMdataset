MOD = 10 ** 9 + 7
s = input()
a = 0
ql = 0
c = s.count('C')
qr = s.count('?')
ans = 0 
for si in s:
    if si == '?':
        qr -= 1
    if si in 'B?':
        ans = (ans + pow(3,ql+qr,MOD)*a*c 
             + (pow(3,ql+qr-1,MOD)*(ql*c+a*qr) if ql + qr - 1 >= 0 else 0)
             + (pow(3,ql+qr-2,MOD)*ql*qr if ql + qr - 2 >= 0 else 0)) % MOD
    if si == '?':
        ql += 1
    elif si == 'A':
        a += 1
    elif si == 'C':
        c -= 1
print(ans)