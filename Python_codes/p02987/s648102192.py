s = list(input())
ss = set(s)
if len(ss) != 2:
    print('No')
    exit()

for s1 in ss:
    if s.count(s1) != 2:
        print('No')
        exit()

print('Yes')
