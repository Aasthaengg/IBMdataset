S = input()
S = S.replace('BC', 'D')

cnt_a = 0
ans = 0
for i in range(len(S)):
    if S[i] == 'A':
        cnt_a += 1
    elif S[i] == 'D':
        ans += cnt_a
    else:
        cnt_a = 0

print(ans)
