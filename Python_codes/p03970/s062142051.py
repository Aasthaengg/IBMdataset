# CODE FESTIVAL 2016 予選 B: A – Signboard
s = input()
s_correct = 'CODEFESTIVAL2016'

iterations = 0

for i in range(len(s)):
    if s[i] != s_correct[i]:
        iterations += 1

print(iterations)