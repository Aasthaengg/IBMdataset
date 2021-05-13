N = int(input())
S = input()
T = input()
kouho = []
for i in range(len(S)):
    ok = 1
    for j in range(0, len(S)-i):
        if S[i+j] == T[j]:
            continue
        ok = 0
        break
    if ok == 0:
        continue
    break
if ok == 1:
    ans = i+len(T)
else:
    ans = len(S)+len(T)
print(ans)
