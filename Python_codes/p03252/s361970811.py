s = input()
t = input()
l = len(s)
cs = [0]*26
ct = [0]*26
for i in range(l):
    cs[ord(s[i])-ord('a')] += 1
    ct[ord(t[i])-ord('a')] += 1
cs.sort()
ct.sort()
if cs==ct:
    print('Yes')
else:
    print('No')