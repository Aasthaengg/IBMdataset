#072_b
s = input()
a = []
if s.islower() and 1 <= len(s) and len(s) <= 10 ** 5:
    b=""
    for n in range(len(s)):
        if n % 2 == 0:
            a.append(s[n])
    for m in range(len(a)):
        b=b+a[m]
    print(b)
