s = input()[::-1]
n = len(s)
idx = 0
while idx < n:
    if s[idx:idx+5] == 'maerd':
        idx += 5
    elif s[idx:idx+7] == 'remaerd':
        idx += 7
    elif s[idx:idx+5] == 'esare':
        idx += 5
    elif s[idx:idx+6] == 'resare':
        idx += 6
    else:
        print("NO")
        exit()
print("YES")

