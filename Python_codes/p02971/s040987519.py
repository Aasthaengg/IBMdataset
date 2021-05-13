n = int(input())
lis = [int(input()) for i in range(n)]
lis_2 = sorted(lis,reverse = True)
fmax = lis_2[0]
smax = lis_2[1]
for i in range(n):
    if lis[i] == fmax:
        print(smax)
    else:
        print(fmax)