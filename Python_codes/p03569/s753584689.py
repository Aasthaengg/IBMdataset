S = input()
N = len(S)
i = 0
j = N-1
ans = 0
while i < j:
    if S[i] == 'x' and S[j] != 'x':
        ans += 1
        i += 1
    elif S[i] != 'x' and S[j] == 'x':
        ans += 1
        j -= 1
    elif S[i] == S[j]:
        i += 1
        j -= 1
    else:
        ans = -1
        break
print(ans)
