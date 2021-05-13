s = input()

if len(s) < 26:
    for i in range(26):
        c = chr(ord('a') + i)
        if not c in s:
            print(s + c)
            exit()
elif s == 'zyxwvutsrqponmlkjihgfedcba':
    print(-1)
    exit()
else:
    for i in range(24,-1,-1):
        for j in range(25,i,-1):
            if s[i] < s[j]:
                print(s[:i] + s[j])
                exit()

