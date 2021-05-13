from math import log

n = float(input())
a = log(n, 26)

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
out = []
while (n):
    n-=1
    out.append(alphabet[int(n%26)])
    n //= 26
out.reverse()

print("".join(out))
