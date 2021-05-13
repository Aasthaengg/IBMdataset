S = input()
ans = 0
for s, t in zip(S, 'CODEFESTIVAL2016'):
    if s != t: ans += 1
print(ans)