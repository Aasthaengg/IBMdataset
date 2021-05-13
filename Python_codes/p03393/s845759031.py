S = input()

if len(S) < 26:
    for i in range(26):
        if chr(i+97) not in S:
            ans = S + chr(i+97)
            break
elif S == "zyxwvutsrqponmlkjihgfedcba":
    ans = -1
else:
    ans = ""
    L = [S[-1]]
    for i in range(24, -1, -1):
        for l in L:
            if S[i] < l:
                for j in range(i):
                    ans += S[j]
                ans += l
                break
        if ans:
            break
        L.append(S[i])
        L.sort()
print(ans)