from math import log10
N=input()

if log10(int(N)) % 1==0:
    print("10")
else:
    print(sum(map(int, list(N))))
