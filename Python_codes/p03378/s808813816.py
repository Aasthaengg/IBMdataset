N, M, X = map(int, input().split(' '))
A = list(map(int, input().split(' ')))

r_count = 0
l_count = 0

tmp_1 = X
tmp_2 = X


while tmp_1 != N:
    tmp_1 += 1
    if tmp_1 in A:
        r_count += 1

while tmp_2 != 0:
    tmp_2 -= 1
    if tmp_2 in A:
        l_count += 1


res = min(l_count, r_count)
print(res)
