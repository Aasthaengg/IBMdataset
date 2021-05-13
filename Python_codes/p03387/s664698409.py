a = list(map(int , input().split()))
maxa = max(a)
x = sum(map(lambda x: maxa-x, a))

if x % 2 == 0:
    print(x // 2)
else:
    print((x+3) // 2)
