s = input()

cnt_0 = 0
cnt_1 = 0

for i in range(len(s)):
    if s[i] == "0":
        cnt_0 += 1
    else:
        cnt_1 += 1

print(2*min(cnt_0, cnt_1))
