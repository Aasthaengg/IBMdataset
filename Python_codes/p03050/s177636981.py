def make_divisors(n):
    # from qiita.com/LorseKudos
    l, u = [], []
    i = 1
    while i*i<=n:
        if n%i==0:
            l.append(i)
            if i!=n//i:
                u.append(n//i)
        i+=1
    return l+u[::-1]

n = int(input())
Ns = make_divisors(n)
Ns = [_ns-1 for _ns in Ns if _ns!=1]
ans = 0
for _ns in Ns:
    if n//_ns==n%_ns:
        ans += _ns
print(ans)