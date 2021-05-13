a, b, t = map(int,input().split())

if t < a:
    print(0)

else:
    print(int(b * ((t + 0.5) // a)))
