import string
charset = string.ascii_lowercase
s = list(input())

unused = set(charset) - set(s)

if unused:
    s.append(min(unused))
    print(''.join(s))
    exit()
else:
    length = len(s)
    
    cand=[s[-1]]
    for i in range(length-1):
        if s[length-i-2] < s[length-i-1]:
            # candからs[length-i-2]より大きく、最小の値を選ぶ
            s[length-i-2] = min([c for c in cand if c>s[length-i-2]])
            print(''.join(s[:length-i-1]))
            exit()
        cand.append(s[length-i-2])
print(-1)