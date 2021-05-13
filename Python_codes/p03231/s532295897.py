def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

n, m = map(int, input().split())
s = list(input())
t = list(input())
g = gcd(n, m)
l = lcm(n, m)
x_s = [i for i in range(1, l + 1, m // g)]
x_t = [i for i in range(1, l + 1, n // g)]
j = 0
c = 1
for i in range(len(x_s)):
    while True:
        if j + 1 == len(x_t):
            break
        if x_s[i] > x_t[j]:
            j += 1
        else:
            break
    if x_s[i] == x_t[j]:
        if not s[i] == t[j]:
            c = 0
print(l if c == 1 else -1)