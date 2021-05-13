s = input()
t = input()

resolved = False
for i in (range(len(s) - len(t) + 1)):
    sliced = s[len(s)-len(t)-i:len(s)-i]
    matched = True
    for j in range(len(sliced)):
        if sliced[j] != t[j] and sliced[j] != '?':
            matched = False
            break
    if matched:
        resolved = True
        s = s[:len(s)-len(t)-i] + t + s[len(s)-i:]
        break

if resolved:
    print(s.replace('?', 'a'))
else:
    print('UNRESTORABLE')

