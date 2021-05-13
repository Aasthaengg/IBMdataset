il = input().split()
N = int(il[0])
R = int(il[1])

if (N >= 10):
    print(R)
else:
    print(R + 100*(10-N))
