S = input()
S1 = [s for s in S if s != 'x']
# print(S, S1)

ans = 0
ls = len(S)
l = 0
r = ls - 1
while l < r:
    if S[l] == S[r]:
        l += 1
        r -= 1
        continue
    if S[l] == 'x':
        l += 1
        ans += 1
    elif S[r] == 'x':
        r -= 1
        ans += 1
    else:
        ans = -1
        break
print(ans)
