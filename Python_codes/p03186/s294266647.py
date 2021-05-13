# AGC 030: A – Poisonous Cookies
a, b, c = [int(i) for i in input().split()]

if c <= a + b:
    print(b + c)
else:
    print(a + b * 2 + 1)
