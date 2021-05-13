from sys import stdin
import fractions

#最小公倍数
def lcm(x, y):
    return (x * y) // fractions.gcd(x, y)

n,m = [int(x) for x in stdin.readline().rstrip().split()]
s = stdin.readline().rstrip()
t = stdin.readline().rstrip()
koubai = lcm(n,m)

if s[::koubai//m] == t[::koubai//n]:
    print(koubai)
else:
    print(-1)