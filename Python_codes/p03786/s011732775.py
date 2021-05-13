n, *aa = map(int, open(0).read().split())

aa.sort()

count = 1
tmp = aa[0]
for i in range(1,n):
    if 2 * tmp >= aa[i]:
        tmp += aa[i]
        count += 1
    else:
        tmp += aa[i]
        count = 1
#     print(count, tmp)

print(count)