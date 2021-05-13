n = int(input())
V = map(int, input().split())

odd = []
even = []
for i, v in enumerate(V):
    if i % 2 == 0:
        odd.append(v)
    else:
        even.append(v)
num_odd = {}
for v in odd:
    if v in num_odd:
        num_odd[v] += 1
    else:
        num_odd[v] = 1
num_even = {}
for v in even:
    if v in num_even:
        num_even[v] += 1
    else:
        num_even[v] = 1
val_odd = sorted(num_odd.items(), key=lambda x:x[1])
val_even = sorted(num_even.items(), key=lambda x:x[1])
if len(val_odd) == 1 and len(val_even) == 1:
    if val_odd[0][0] == val_even[0][0]:
        # 全部同じ値 -> 半分変化させる
        print(n // 2)
    else:
        # すでに整ってる
        print(0)
else:
    # 奇数・偶数ともに必要なだけ変化させる
    if val_odd[-1][0] != val_even[-1][0]:
        # 最も多い値が違う場合はそれぞれその値を増やせばいい
        count_odd = n // 2 - val_even[-1][1]
        count_even = n // 2 - val_odd[-1][1]
        print(count_odd + count_even)
    else:
        # 同じ場合は、少ない方の第二頻出値を増やす
        c1 = n - val_odd[-1][1] - val_even[-2][1]
        c2 = n - val_odd[-2][1] - val_even[-1][1]
        print(min(c1, c2))
