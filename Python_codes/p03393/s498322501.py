s = input()
if len(s)<26:
    seen = set()
    for c in s:
        seen.add(c)
    for i in range(26):
        tmp = chr(i+ord('a'))
        if tmp not in seen:
            print(s+tmp)
            break
else:
    pre = 'a'
    seen = set()
    for i, c in enumerate(reversed(s)):
        if c < pre:
            for j in range(26):
                tmp = chr(j+ord(c)+1)
                if tmp in seen:
                    print(s[:25-i]+tmp)
                    break
            break
        seen.add(c)
        pre = c
    else:
        print(-1)