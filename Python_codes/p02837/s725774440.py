from itertools import product

N = int(input())
testimony_by = []   # i番目の人の発言を格納する(3次元リスト)
for i in range(N):
    a = int(input())
    li = []   # 発言一つ分のリスト
    for j in range(a):
        li.append(list(map(int, input().split())))
    testimony_by.append(li)
ans = 0
for bit_li in product([0, 1], repeat=N):
    is_ok = True    # 矛盾がないか
    for i in range(N):
        if bit_li[i] == 1:
            for li in testimony_by[i]:
                x, y = li
                x -= 1
                if bit_li[x] != y:
                    is_ok = False
                    break

        if not is_ok:
            break
    if is_ok:
        ans = max(ans, sum(bit_li))
print(ans)
