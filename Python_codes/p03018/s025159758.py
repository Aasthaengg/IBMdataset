s = input().replace('BC', 'D')
s = s.replace('B', 'C')
l = [x for x in s.split(sep='C') if x != '']
ans = 0
for subs in l:
    numA = 0
    for c in subs:
        if c == 'A':
            numA += 1
        elif c == 'D':
            ans += numA

print(ans)