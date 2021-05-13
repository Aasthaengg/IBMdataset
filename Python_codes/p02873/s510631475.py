S = input()
# N, K = [int(_) for _ in input().split()]
count = 1
S2 = []
for i in range(len(S)):
    if i < len(S)-1 and S[i] == S[i+1]:
        count += 1
    else:
        if S[i] == '<':
            S2.append(['<', count])
        else:
            S2.append(['>', count])
        count = 1
ans = 0
for i in range(len(S2)):
    if S2[i][0] == '<':
        if i < len(S2)-1:
            if S2[i][1] < S2[i+1][1]:
                ans += (S2[i][1] - 1) * (S2[i][1] - 0) // 2
            else:
                ans += S2[i][1] * (S2[i][1] + 1) // 2
        else:
            ans += S2[i][1] * (S2[i][1] + 1) // 2
    else:
        if i > 0:
            if S2[i-1][1] >= S2[i][1]:
                ans += (S2[i][1] - 1) * (S2[i][1] - 0) // 2
            else:
                ans += S2[i][1] * (S2[i][1] + 1) // 2
        else:
            ans += S2[i][1] * (S2[i][1] + 1) // 2
print(ans)


