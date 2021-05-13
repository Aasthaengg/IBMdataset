import fractions

n,m = map(int, input().split())
s = input()
t = input()

gcd = fractions.gcd(n,m)

print(n*m//gcd if all([s[i*n//gcd]==t[i*m//gcd] for i in range(gcd)]) else -1)