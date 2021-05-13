import sys

S_ = input()
T = input()

ans = 'UNRESTORABLE'
if len(S_) < len(T):
    print(ans)
    sys.exit()

S = []
for i in range(len(S_) - len(T) + 1):
    for j in range(len(T)):
        if S_[i + j] == '?' or S_[i + j] == T[j]:
            continue
        else: break
    else:
        tmp = S_[0:i] + T + S_[i + len(T):len(S_)]
        S.append(tmp.replace('?', 'a'))

if len(S) > 0:
    sort = sorted(S)
    ans = sort[0]

print(ans)