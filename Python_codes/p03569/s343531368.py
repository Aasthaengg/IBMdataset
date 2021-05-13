S = list(input())

ans = 0

while len(S) > 1:
    if S[0] == S[-1]:
        S.pop(0)
        S.pop(-1)
    elif S[0] == 'x':
        ans += 1
        S.pop(0)
    elif S[-1] == 'x':
        ans += 1
        S.pop(-1)
    else:
        ans = -1
        break

print(ans)
