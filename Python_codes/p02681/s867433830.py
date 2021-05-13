s = input()
t = input()
p = t.find(s)
if p == 0 and len(t) == len(s) + 1 and len(t) > 0 and len(t) <=11:
    print('Yes')
else:
    print('No')