l=[int(x) for x in raw_input().split(" ")]

def gcd(a,b):
    if a > b:
        mod = a % b
        if mod==0: return b
        return gcd(b, mod)
    else:
        mod = b % a
        if mod==0: return a
        return gcd(a, mod)

print gcd(l[0], l[1])