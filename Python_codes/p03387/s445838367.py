a_L = map(int,input().split())

a_L = list(sorted(a_L))

diff1 = a_L[2]-a_L[1]
diff2 = a_L[2]-a_L[0]


if (diff1+diff2) % 2 == 0:
    print((diff1+diff2)//2)
else:
    print((diff1+diff2+3)//2)