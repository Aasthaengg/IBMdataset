S = input()

A = []

ok = 1
ans = 0
cnt = 0
for i in range(len(S)):
    if ok == 1 and i < len(S)-1 and S[i] == 'B' and S[i+1] == 'C':
        A.append('B')
        ans += cnt
    elif S[i] == 'A':
        A.append('A')
        cnt += 1
        ok = 1
    elif ok == 1 and i > 0 and S[i-1] == 'B' and S[i] == 'C':
        continue
    else:
        A = []
        cnt = 0
        ok = 0

print(ans)