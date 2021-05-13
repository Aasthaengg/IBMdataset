S = list(input())
l = len(S)
if S == list('zyxwvutsrqponmlkjihgfedcba'):
    print(-1)
else:
    if l != 26:
        for i in range(26):
            if not chr(i+97) in S:
                S.append(chr(i+97))
                break
        print(''.join(S))
    else:
        li = []
        for i in range(26):
            c = S.pop()
            li.append(c)
            for x in li:
                if x>c:
                    S.append(x)
                    print(''.join(S))
                    break
            else:
                continue
            break    