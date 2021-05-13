S = input()

if len(S) < 26:
    for c in [chr(i) for i in range(ord('a'), ord('a') + 26)]:
        # print(c)
        if c not in S:
            ans = S + c
            break
elif S == 'zyxwvutsrqponmlkjihgfedcba':
    ans = -1
else:
    for i in range(1, len(S)):
        j = - i
        if ord(S[j - 1]) < ord(S[j]):
            break
    # print(S[j:])
    change = 'z'
    for c in S[j:]:
        if ord(S[j - 1]) < ord(c) < ord(change):
            change = c
    ans = S[:j - 1] + change
print(ans)