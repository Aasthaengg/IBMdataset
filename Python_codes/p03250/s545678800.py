a, b, c = map(int, input().split())

f = max(a, b, c)
if f == a:
    print(a*10 + int(str(b+c)))
elif f == b:
    print(b*10 + int(str(a+c)))
else:
    print(c*10 + int(str(b+a)))