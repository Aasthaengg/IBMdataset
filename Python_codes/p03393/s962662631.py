s = input()
word = [0] * 26
for i in s:
    word[ord(i) - ord('a')] = 1

if sum(word) != 26:
    for i in range(26):
        if word[i] == 0:
            c = chr(i + ord('a'))
            break
    print(s + c)
else:
    if s == 'zyxwvutsrqponmlkjihgfedcba':
        print(-1)
    else:
        for i in range(25, -1, -1):
            if s[i] == 'z':
                pass
            else:
                now = ord(s[i]) + 1
                for j in range(now, ord('z')+1):
                    if chr(j) in s[0:i]:
                        pass
                    else:
                        print(s[0:i] + chr(j))
                        exit()
