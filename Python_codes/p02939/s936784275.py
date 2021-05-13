S = input()

ans = 1
looking = S[0]
before = False

for i in range(1, len(S)):
    if before:
        looking = S[i - 1] + S[i]
        before = False
        ans += 1
        continue

    if looking == S[i]:
        before = True
    else:
        ans += 1
        looking = S[i]
print(ans)

