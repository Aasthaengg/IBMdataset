
s=list(str(input()))

nax=len(s)
first=0
last=nax
for i in range(nax):
    if s[i]=='A':
        first=i
        break
for i in range(nax):
    if s[nax-1-i]=='Z':
        last=nax-i-1
        break

print(last-first+1)