S = input()

alf = set([chr(i) for i in range(ord('a'), ord('z')+1)])

if S == "zyxwvutsrqponmlkjihgfedcba":
    print(-1)
elif len(S) < 26:
    not_used_alf = list(alf - set(S))
    ans = S + min(not_used_alf)
    print(ans)
else:
    tmp = S[-1]
    for i in reversed(range(26)):
        if S[i] >= tmp:
            tmp = S[i]
            continue
        else:
            break
    tmp = set(S[i+1:])
    for x in [chr(i) for i in range(ord('a'), ord('z')+1)]:
        if x in tmp and x > S[i]:
            ans = S[:i] + x
            break
    print(ans)