s = input()
s_set = set(s)

for e in s_set:
    if s.count(e) != 2:
        print('No')
        break
else:
    print('Yes')
