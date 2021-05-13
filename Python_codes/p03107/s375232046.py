S = input()
cnt1 = 0
cnt0 = 0
for s in S:
    if s == '1':
        cnt1 += 1
    else:
        cnt0 += 1
print(min(cnt1, cnt0) * 2)