def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

s = map(int, raw_input().split())
if s[0] < s[1]:
    print "%d" % gcd(s[1], s[0])
else:
    print "%d" % gcd(s[1], s[0])