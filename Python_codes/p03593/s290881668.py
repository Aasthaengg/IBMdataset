h, w = map(int, input().split())
str_array = [input() for i in range(h)]
count = [0 for i in range(26)]
for i in range(h):
    for j in range(w):
        count[ord(str_array[i][j]) - ord('a')] += 1

flag = True
count_odd = 0
count_two = 0
if h == 1 and w == 1:
    # 必ずよい
    pass
elif h == 1 or w == 1:
    # 奇数が1種類のみあればいい
    for i in range(26):
        if count[i] % 2 != 0:
            count_odd += 1
            if count_odd > 1:
                flag = False
elif h % 2 == 0 and w % 2 == 0:
    # 全て4の倍数であればよい
    for i in range(26):
        if count[i] % 4 != 0:
            flag = False
elif h % 2 != 0 and w % 2 != 0:
    for i in range(26):
        if count[i] % 2 != 0:
            count_odd += 1
            if count_odd > 1:
                flag = False
        elif count[i] % 4 != 0:
            count_two += 2
            if count_two > h + w - 2:
                flag = False
elif h % 2 != 0:
    for i in range(26):
        if count[i] % 2 != 0:
            flag = False
        elif count[i] % 4 != 0:
            count_two += 2
            if count_two > w:
                flag = False
elif w % 2 != 0:
    for i in range(26):
        if count[i] % 2 != 0:
            flag = False
        elif count[i] % 4 != 0:
            count_two += 2
            if count_two > h:
                flag = False

if flag:
    print("Yes")
else:
    print("No")
