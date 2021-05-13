s=input()
s=s.replace("BC", "D")
ans=0
a=0
for c in s:
    if c=='A': a+=1
    elif c=='D': ans+=a
    else: a=0
print(ans)