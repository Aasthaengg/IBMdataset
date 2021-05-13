a, b, c = [int(i) for i in input().split()]
if b >= c:
    count = c + (b-(b-c))
    c = 0
else:
    count = (c-(c-b))*2
    c -= b
b -= count//2
if c >= a and a > 0:
    count += c-(c-a)
    c -= c-(c-a)
    print(count + (1 if c else 0))
elif a > c and c > 0:
    print(count+(a-(a-c)))
else:
    print(count+b)