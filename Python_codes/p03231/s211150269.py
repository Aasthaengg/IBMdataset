import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0
def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)
def lcm(a,b):
    return (a//gcd(a,b)*b)
n,m = map(int,readline().split())
s = readline().rstrip().decode('utf-8')
t = readline().rstrip().decode('utf-8')
l = lcm(n,m)
g = gcd(n,m)
flag = 1

for i in range((n-1)//(n//g)+1):
    if not s[i*(n//g)] == t[i*(m//g)]:
        flag = 0
        break


if flag:
    print(l)
else:
    print(-1)