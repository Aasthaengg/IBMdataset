L = list(map(int,input().split()))
L.sort()
if L[2] / L[1] == 1:
    print(L[0])
else:print(L[2])