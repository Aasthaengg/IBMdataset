S = input()
prev = S[0]
S = S[1:]
ans = 1
while len(S)>0:
    i = 1
    while True:
        if prev == S[:i] and len(S) > 1:
            i += 1
        else:
            break
    if prev != S[:i]:
        ans += 1
        prev = S[:i]
    S = S[i:]
print(ans)