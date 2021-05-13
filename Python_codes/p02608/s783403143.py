n=int(input())
l = [0] * 10001
for a in range(1, 101):
    for b in range(1,101):
        for c in range(1, 101):
            o = a**2 + b**2 + c**2 + a*b + a*c + c*b
            if o <= 10000:
                l[o] += 1
for i in range(1, n+1):
    print(l[i])