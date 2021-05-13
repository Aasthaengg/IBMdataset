n = int(input())
a = list(map(int, input().split()))

ans = 0
dic1 = {}
dic2 = {}
for i in range(n):
    tmp1 = a[i] + (i + 1)
    tmp2 = -a[i] + (i + 1)
    if tmp1 in dic1:
        dic1[tmp1] += 1
    else:
        dic1[tmp1] = 1
    if tmp2 in dic2:
        dic2[tmp2] += 1
    else:
        dic2[tmp2] = 1
for key in dic1.keys():
    if key in dic2:
        ans += dic1[key] * dic2[key]
print(ans)
