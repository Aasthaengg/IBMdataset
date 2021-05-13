s = input()
t = input()

for i in range(len(s) - len(t) + 1)[::-1]:
    cnt = 0
    for ns, nt in zip(s[i:i+len(t)], t):
        cnt += 1
        if ns != nt and ns != '?':
            break
        if cnt == len(t):
            ans = s[:i] + t + s[i+len(t):]
            print(ans.replace('?', 'a'))
            exit()
print('UNRESTORABLE')
