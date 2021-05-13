S = input()
remaining = set("abcdefghijklmnopqrstuvwxyz") - set(S)
if remaining:
    print(S + min(remaining))
else:
    prev = S[25]
    for i in range(24, -1, -1):
        c = S[i]
        if c < prev:
            print(S[:i] + min(c for c in S[i + 1 :] if c > S[i]))
            break
        prev = c
    else:
        print(-1)
