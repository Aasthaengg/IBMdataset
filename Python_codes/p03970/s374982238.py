S = input()

correct_s = 'CODEFESTIVAL2016'

ans = 0
for s1, s2 in zip(S, correct_s):
    if s1 != s2:
        ans += 1

print(ans)

