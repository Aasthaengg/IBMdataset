N = input()
tmp = len(N) - 1
NL = list(N)
if len(N) == 1:
    print(int(N))
elif all(x == "9" for x in NL[1:]):
    print(int(N[0]) + tmp * 9)
else:
    print(int(N[0]) - 1 + tmp * 9)