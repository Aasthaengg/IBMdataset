ans_word = "keyence"

s = input()
flag = False
if s == ans_word:
    flag = True
else:
    for i in range(len(s)-1):
        for j in range(i+1, len(s)):
            if s[:i] + s[j:] == ans_word:
                flag = True
                break
        if flag:
            break

if flag:
    print("YES")
else:
    print("NO")
