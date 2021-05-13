n = int(input())
multi2 = multi4 = 0
for i in map(int, input().split()):
    if i % 4 == 0:
        multi2 += 1
        multi4 += 1
    elif i % 2 == 0:
        multi2 += 1

res = 'No'
if multi4 >= n // 2 or multi2 == n:
    res = 'Yes'
elif multi4 >= (n - (multi2 - multi4)) / 2:
    res = 'Yes'
print(res)
