s = raw_input()
p = raw_input()
ss = s + s
ps = p[0]
ret = 'No'
for i in range(len(s)):
    if s[i] == ps:
        c = 0
        for k in range(len(p)):
            if ss[i+k] == p[k]:
                c = c + 1
        if c == len(p):
            ret = 'Yes'
print ret