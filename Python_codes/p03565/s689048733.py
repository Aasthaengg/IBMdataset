s = input()
t = input()

for i in range(len(s) - len(t) + 1)[::-1]:
    for j, (ns, nt) in enumerate(zip(s[i:i+len(t)], t)):
        if ns != nt and ns != '?':
            break
        if j == len(t) -1:
            ans = s[:i] + t + s[i+len(t):]
            print(ans.replace('?', 'a'))
            exit()
print('UNRESTORABLE')
