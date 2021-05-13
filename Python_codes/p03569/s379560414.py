*s, = input()

i = 0
j = -1
n = len(s)
ans = 0

while n > 0:
    if s[i] == s[j]:
        i += 1
        j -= 1
        n -= 2
    else:
        ans += 1
        if s[i] == 'x':
            i += 1
            n -= 1
        elif s[j] == 'x':
            j -= 1
            n -= 1
        else:
            ans = -1
            break

print(ans)