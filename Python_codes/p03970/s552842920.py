s = input()

correct = 'CODEFESTIVAL2016'
cnt = 0
for i in range(len(s)):
    if s[i] != correct[i]:
        cnt += 1

print(cnt)