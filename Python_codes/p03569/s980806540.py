s = input()

i = 0
j = len(s) - 1
ans = 0
while i != j:
    if abs(i - j) == 1:
        if s[i] == s[j]:
            break
    if s[i] != s[j]:
        if s[i] != "x" and s[j] != "x":
            print(-1)
            exit()
        elif s[i] != "x":
            j -= 1
        else:
            i += 1
        ans += 1
    else:
        i += 1
        j -= 1

print(ans)