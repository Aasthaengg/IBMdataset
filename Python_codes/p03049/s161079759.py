n = int(input())
s = [input() for i in range(n)]

ab = 0
ba = 0
c2 = 0
c3 = 0
for x in s:
    if 'AB' in x:
        ab += x.count('AB')    
    if x[-1] == 'A' and x[0] == 'B':
        ba += 1
    if x[-1] == 'A' and x[0] != 'B':
        c2 += 1
    if x[-1] != 'A' and x[0] == 'B':
        c3 += 1
if ba > 0:
    if c2 + c3 > 0:
        ans = ab + ba + min(c2, c3)
    else: # c2 = c3 =0
        ans = ab + ba - 1
else:
    ans = ab + min(c2, c3)
print(ans)