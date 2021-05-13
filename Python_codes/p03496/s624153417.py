n = int(input())
a = list(map(int, input().split()))

ma = max(a)
mi = min(a)

num = 0
ans = []

if ma >= -mi:
    ind = a.index(ma)
    for i in range(1, n):
        while a[i-1] > a[i]:
            num += 1
            ans.append(str(ind+1) + ' ' + str(i+1))
            a[i] += ma
            if a[i] > ma:
                ma = a[i]
                ind = i

else:
    ind = a.index(mi)
    for i in range(n-2, -1, -1):
        while a[i] > a[i+1]:
            num += 1
            ans.append(str(ind+1) + ' ' + str(i+1))
            a[i] += mi
            if a[i] < mi:
                mi = a[i]
                ind = i

print(num)
for i in ans:
    print(i)