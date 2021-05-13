N = int(input())
S = []
for _ in range(N):
    S.append(input())
for i in range(N):
    S[i] = sorted(S[i])
S = sorted(S)
ans = 0
sa = 1
for i in range(N):
    if i == N-1:
        if sa == 1:
            break
        else:
            ans += int(sa * (sa - 1) / 2)
            break
    if S[i] == S[i+1]:
        sa += 1
    else:
        if sa == 1:
            continue
        else:
            ans += int(sa * (sa - 1) / 2)
            sa = 1
print(ans)