n = int(input())
s = input()
right_w = 0
right_E = 0
left_E = 0
left_W = 0
ans = len(s)
for i in s:
    if i == "W":
        right_w += 1
    else:
        right_E += 1
for i in range(len(s)):
    tmp = s[i]
    if tmp == 'W':
        right_w -= 1
        tmp_ans = left_W+ right_E
        if tmp_ans < ans:
            ans = tmp_ans
        left_W += 1
    else:
        right_E -= 1
        tmp_ans = left_W+ right_E
        if tmp_ans < ans:
            ans = tmp_ans
        left_E += 1
print(ans)