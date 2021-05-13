S = input()
cnt = 0
for idx, val in enumerate(S):
        if val != 'CODEFESTIVAL2016'[idx]:
                cnt += 1

print(cnt)
