s = input()
t = input()

if len(t) > len(s):
    print('UNRESTORABLE')
    exit()

s = s[::-1]
t = t[::-1]

for i in range(len(s) - len(t) + 1):
    j = 0
    while True:
        if j == len(t):
            ans = s[:i] + t + s[i+len(t):]
            print(ans[::-1].replace('?', 'a', len(ans)))
            exit()
        if t[j] == s[i+j] or s[i+j] == '?':
            j += 1
        else:
            break
print("UNRESTORABLE")