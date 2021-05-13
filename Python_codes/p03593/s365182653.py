h, w = map(int, input().split())
a = [[j for j in input()] for i in range(h)]

cnt = [0 for i in range(26)]
for i in range(h):
    for j in range(w):
        cnt[ord(a[i][j]) - ord("a")] += 1

ans1 = 0
ans2 = 0
ans4 = 0
if h % 2 == 1 and w % 2 == 1:
    ans1 = 1
    ans2 = (h - 1) // 2 + (w - 1) // 2
    ans4 = (h * w - ans1 - ans2 * 2) // 4
elif h % 2 == 1:
    ans2 = w // 2
    ans4 = (h * w - ans2 * 2) // 4
elif w % 2 == 1:
    ans2 = h // 2
    ans4 = (h * w - ans2 * 2) // 4
else:
    ans4 = h * w // 4

cnt1 = 0
cnt2 = 0
cnt4 = 0
for i in cnt:
    if i >= 4:
        cnt4 += i // 4
        i %= 4
    if i >= 2:
        cnt2 += i // 2
        i %= 2
    cnt1 += i

# print("ans1 =", ans1)
# print("ans2 =", ans2)
# print("ans4 =", ans4)
# print("cnt1 =", cnt1)
# print("cnt2 =", cnt2)
# print("cnt4 =", cnt4)

if ans4 > cnt4:
    print("No")
else:
    cnt2 += (cnt4 - ans4) * 2
    if ans2 > cnt2:
        print("No")
    else:
        cnt1 += (cnt2 - ans2) * 2
        if ans1 != cnt1:
            print("No")
        else:
            print("Yes")