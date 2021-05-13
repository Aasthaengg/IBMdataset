n = int(input())
a = list(map(int,input().split()))
an = max(a)
mi = -1
ms = 10**10
an2 = an/2
for i in a:
    if ms > abs(i-an2) and not an == i:
        mi = i
        ms = abs(i-an2)

print(an,mi)
