s=input()
s=s[:-1]

if len(s)%2==1:
    s=s[:-1]
while len(s)>=0:
    l=len(s)//2
    if s[:l]==s[l:]:
        break
    s=s[:-1]
    s=s[:-1]
print(len(s))
