n = int(input())
a = [int(input()) for i in range(n)]

amax1 = max(a)
amax_i1 = a.index(amax1)

a.pop(amax_i1)
amax2 = max(a)
amax_i2 = a.index(amax2)

for i in range(n):
    if i == amax_i1:
        print(amax2)
    else:
        print(amax1)