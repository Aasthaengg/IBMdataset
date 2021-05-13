S = list(input())
T = list(input())

ans = 'No'
for i in range(len(S)):
    s = S.pop(len(S)-1)
    S.insert(0, s)
    if S == T:
        ans = 'Yes'
        break
print(ans)
