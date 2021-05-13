n, k = map(int, input().split())
a = list(map(int, input().split()))

dct = {}
for i in range(n):
    if a[i] in dct:
        dct[a[i]] += 1
    else:
        dct[a[i]] = 1
select_num = len(dct) - k
if select_num <= 0:
    print(0)
    exit()
sorted_dct = sorted(dct.items(), key=lambda x:x[1])
ans = 0
for i in range(select_num):
    ans += sorted_dct[i][1]
print(ans)