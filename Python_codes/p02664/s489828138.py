t = list(input())
ans = [0] * len(t)
for i in range(len(t)):
    if t[i] != '?':
        ans[i] = t[i]
    else:
        ans[i] = 'D'

print(''.join(ans))