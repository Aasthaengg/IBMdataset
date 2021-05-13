import string
S = input()
if len(S) == 26:
    if S == "zyxwvutsrqponmlkjihgfedcba":
        print(-1)
    else:
        i = len(S) - 1
        while 0 <= i:
            if S[i-1] < S[i]:
                break
            i -= 1
        ans = ""
        for x in range(i):
            ans += S[x]

        for j in S[i:][::-1]:
            if ans[-1] < j:
                ans = ans[:-1] + j
                break

        print(ans)

    exit()

chars_set = set(S)
for c in string.ascii_lowercase:
    if c not in chars_set:
        S += c
        break
print(S)