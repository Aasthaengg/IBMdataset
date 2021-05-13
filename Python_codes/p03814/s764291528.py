s = str(input())

for i in s:
    if i == 'A':
        x = s.index(i)
        break
for h in range(len(s)-1,-1,-1):
    if s[h] == 'Z':
        y = h
        break
print(y-x+1)