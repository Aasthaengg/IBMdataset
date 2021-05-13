n = int(input())
a = [int(i) for i in input().split()]
ans1 = 0
ans2 = 0
summ = 0
summ2 = 0
a2 = a[:]


for i in range(n):
    if i % 2 == 0:
        if summ + a[i] <= 0:
            ans1 += abs(summ + a[i]) + 1
            a[i] = -summ + 1
            summ = 1
        else:
            summ += a[i]
    else:
        if summ + a[i] >= 0:
            ans1 += abs(summ + a[i]) + 1
            a[i] = -summ -1
            summ = -1
        else:
            summ += a[i]
#-+-
for i in range(n):
    if i % 2 != 0:
        if summ2 + a2[i] <= 0:
            ans2 += abs(summ2 + a2[i]) + 1
            a2[i] = -summ2 + 1
            summ2 = 1
        else:
            summ2 += a2[i]
    else:
        if summ2 + a2[i] >= 0:
            ans2 += abs(summ2 + a2[i]) + 1
            a2[i] = -summ2 -1
            summ2 = -1
        else:
            summ2 += a2[i]


print(min(ans1, ans2))
