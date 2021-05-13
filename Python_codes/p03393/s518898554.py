S = input()
if S == "zyxwvutsrqponmlkjihgfedcba":
    print(-1)
    exit()
S = [ord(a)-97 for a in S]
if len(S) < 26:
    for i in range(26):
        if i not in S:
            T = S + [i]
            print("".join([chr(a+97) for a in T]))
            exit()
else:
    for i in range(26)[::-1]:
        for j in range(S[i]+1, 26):
            if j in S[i:]:
                T = S[:i] + [j]
                print("".join([chr(a+97) for a in T]))
                exit()