al = list(map(int, input().split()))
al.sort()

d = al[2] - al[1]
if (al[1]-al[0])%2 == 0:
    print(d + (al[1] - al[0])//2)
else:
    print(d + (al[1] - al[0])//2+2)