a,b,c,d = map(int, input().split())

ab = a * b
cd = c * d

if ab == cd:
    print(int(ab))
elif ab > cd:
    print(int(ab))
else:
    print(int(cd))