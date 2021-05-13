N, Y = map(int, input().split())
Y //= 1000
for nog in range(N + 1):
    for hig in range(N + 1 - nog):
        yuk = N - nog - hig
        if nog + hig * 5 + yuk * 10 == Y:
            print(yuk, hig, nog)
            break
    else:
        continue
    break
else:
    print("-1 -1 -1")