s=input()
K = int(input())
c = []
for i in range(len(s)):
    if s[i]=='a':
        c.append(0)
    else:
        c.append(123-ord(s[i]))
for i in range(len(s)):
    if c[i] <= K:
        K -= c[i]
        c[i]=0
    else:
        continue
if K >0 and c[-1]==0:
    c[i]+= K%26
else:
    c[i] = (-c[i] +K)%26
si = ''
for i in range(len(c)-1):
    if c[i]==0:
        si += 'a'
    else:
        si += s[i]
si += chr(97+c[-1])
print(si)
