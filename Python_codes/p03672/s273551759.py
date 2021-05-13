s = list(input())

for i in range(len(s)):
    if i == 0:
        s.pop()
    elif len(s) % 2 == 0:
        if s[:len(s)//2] == s[len(s)//2:]:
            print(len(s))
            break
        else:
            s.pop()
    else:
        s.pop()