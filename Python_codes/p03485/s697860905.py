a, b = list(map(int, input().split()))

c = (a+b)/2

if int(c) == c:
    print(int(c))
else:
    print(int(c+1))