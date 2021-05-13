n = int(input())
an = list(map(int, input().split()))
ls = [0] * (n+1)
for i in an:
    ls[i] += 1
ms = [i*(i-1)/2 for i in ls]
kei = sum(ms)
for j in an:
    j=ls[j]
    ans = kei - j*(j-1)/2 + (j-2)*(j-1)/2
    print(int(ans))