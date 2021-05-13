S = input()
S_right = 'CODEFESTIVAL2016'

cnt = 0
for si, sri in zip(S, S_right):
    if si != sri:
        cnt += 1

print(cnt)
