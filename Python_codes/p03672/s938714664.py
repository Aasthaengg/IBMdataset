s=input()
f=False
sl=len(s)
while not f:
    sl-=2
    if s[0:sl//2]==s[(sl+1)//2:sl]:
        f=True
print(sl)