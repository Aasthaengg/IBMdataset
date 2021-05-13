#  Copyright: this code was written at 2020. for AtCoder by Silviase


def make_pascal_tri(n):
    array = [[1 for i in range(n + 1)] for i in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(n + 1):
            if j > i:
                array[i][j] = 0
            elif j == 0 or j == i:
                array[i][j] = 1
            else:
                array[i][j] = array[i - 1][j] + array[i - 1][j - 1]
    return array


ar = make_pascal_tri(100)
n, a, b = map(int, input().split())
val = sorted(map(int, input().split()), reverse=True)
res_ave = 0
for i in range(a):
    res_ave += val[i]
res_ave /= a
grat_cnt = 0
same_cnt = 0
for i in range(n):
    if val[i] > val[a - 1]:
        grat_cnt += 1
    elif val[i] == val[a - 1]:
        same_cnt += 1
    else:
        break
result = 0

if grat_cnt == 0:
    for i in range(a, b + 1):
        result += ar[same_cnt][i]
else:
    result = ar[same_cnt][a - grat_cnt]

print(res_ave)
print(result)
