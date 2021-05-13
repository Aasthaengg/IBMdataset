# LRRRRRRL, LRL は同じ(不幸な人は3人)
# L, R で分割してやると一回の操作でLRL -> LLL -> で不幸な人が2人へる LR の時は LLで1人減る
n, k = list(map(int, input().split(' ')))
s = input()

# LLRRRLL -> 1,1,1に変換して合体させていく
old = ''
converted = []
for c in s:
    if old != c:
        converted.append(1)
        old = c
temp = max(len(converted) - 2*k, 1)  # 必ず一人は犠牲になる
print(n - temp)