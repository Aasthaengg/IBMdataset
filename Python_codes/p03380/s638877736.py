#21
n=int(input())
a=list(map(int,input().split()))
a.sort()

m = a[-1]
a_minus_m = [abs(aa-m/2) for aa in a]

mi = 10**10
i_mi=0
for i,aa in enumerate(a_minus_m):
    if aa<mi:
        mi =aa
        i_mi=i

r = a[i_mi]
print(m,r)