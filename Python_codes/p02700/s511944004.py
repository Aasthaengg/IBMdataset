a,b,c,d = map(int, input().split())
i = 0
while True:
    if i % 2 == 0:
        c -= b
    else:
        a -= d
    i += 1
    if a <= 0:
        print("No")
        break
    elif c <= 0:
        print("Yes")
        break
