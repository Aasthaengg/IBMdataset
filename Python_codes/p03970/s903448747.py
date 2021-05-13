s = input()
S = 'CODEFESTIVAL2016'
ans = 0
for c, C in zip(s, S):
    if c != C:
        ans += 1
print(ans)