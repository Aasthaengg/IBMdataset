from sys import exit

s = input()
t = input()

l = len(s)
d_s = dict()
d_t = dict()
for i in range(l):
    if s[i] in d_s:
        if d_s[s[i]] != t[i]:
            print('No')
            exit()
    else:
        d_s[s[i]] = t[i]
    
    if t[i] in d_t:
        if d_t[t[i]] != s[i]:
            print('No')
            exit()
    else:
        d_t[t[i]] = s[i]

print('Yes')