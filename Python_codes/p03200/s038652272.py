S = input()
ans = 0
t = 0
for i in range(len(S)):
    if S[i] == 'W':
        ans += i - t
        t += 1
print(ans)