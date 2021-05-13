n = int(input())
ne = 0
no = 0
a = list(map(int, input().split()))
for ai in a:
    if ai % 2 == 0:
        ne += 1
    else:
        no += 1

# print(n, a, ne, no)

# 奇数はくっつけると偶数になる
odd_rem = no % 2
ne += no // 2

# 偶数はくっつけると偶数になって1つ減るので，1つだけにできる
# ne = 1

# if odd_rem == 1:

# 奇数
if odd_rem == 1:
    print("NO")
else:
    print("YES")