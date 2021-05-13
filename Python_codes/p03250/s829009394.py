a, b, c = map(int, input().split())
print(max(a + (b*10+c), (a*10+b) + c,
a + (c*10+b), (a*10+c) + b,
b + (a*10+c), (b*10+a) + c,
b + (c*10+a), (b*10+c) + a,
c + (a*10+b), (c*10+a) + b,
c + (b*10+a), (c*10+b) + a))

