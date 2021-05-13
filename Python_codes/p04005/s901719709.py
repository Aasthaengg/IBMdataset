a, b, c = map(int, input().split())
if a%2!=0 and b%2!=0 and c%2!=0:
    print(min(a*b, b*c, c*a))
else:
    print(0)