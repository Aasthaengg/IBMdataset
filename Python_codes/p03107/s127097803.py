s = input()
cnt1 = 0
cnt2 = 0
for i in range(len(s)):
    if s[i] == '0':
        cnt1 += 1
    else:
        cnt2 += 1
print(min(cnt1, cnt2)*2)