A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

if A % 10 == 0:
    a = 0
else:
    a = 10 - A % 10

if B % 10 == 0:
    b = 0
else:
    b = 10 - B % 10

if C % 10 == 0:
    c = 0
else:
    c = 10 - C % 10

if D % 10 == 0:
    d = 0
else:
    d = 10 - D % 10

if E % 10 == 0:
    e = 0
else:
    e = 10 - E % 10

sum = A + B + C + D + E + a + b + c + d + e - max(a,b,c,d,e)

print(sum)