s = str(input())
alpha = 'abcdefghijklmnopqrstuvwxyz'
inv_alpha = 'zyxwvutsrqponmlkjihgfedcba'
if len(s) == 26:
    if s == inv_alpha:
        print(-1)
    else:
        for i in reversed(range(25)):
            for j in reversed(range(i+1, 26)):
                if s[i] < s[j]:
                    print(s[:i] + s[j])
                    break
            else:
                continue
            break
else:
    S = sorted(set(alpha) - set(s))
    print(s + S[0])
