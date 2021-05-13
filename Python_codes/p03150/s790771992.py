S = input()
ans = False
for i in range(0, len(S)):
    for j in range(len(S)-i+1):
        ns = S[:j] + S[j+i:]
        if ns == 'keyence':
            ans = True
            break
    if ans:
        break
print('YES' if ans else 'NO')
