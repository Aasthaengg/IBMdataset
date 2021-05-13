n = int(input())
a = [int(i) for i in input().split()]
a.sort()
amax = a[-1]
tmp1 = amax + 1
for i in a[:n-1]:
    tmp2 = i - amax/2
    if tmp2 > tmp1:
        break
    else:
        r = i
        tmp1 = abs(tmp2)
print(amax, r)