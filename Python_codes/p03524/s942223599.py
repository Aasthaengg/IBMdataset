from collections import Counter
S=input()
d = {'a':0,'b':0,'c':0}
for i in S:
    d[i] += 1
if max(d.values())-min(d.values()) <=1:
    print('YES')
else:
    print('NO')