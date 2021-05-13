a, b = map(int, input().split())

if b > a >= 0 or a < b <= 0:
    print(abs(a-b))
elif a > b > 0 or 0 > a > b:
    print(abs(a-b)+2)
else:
    print(abs(abs(a)-abs(b))+1)