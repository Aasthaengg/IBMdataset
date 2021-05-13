s=input()
f1=0
f2=0
ok=True
for i in range(len(s)):
    if s[i]=='A' and ok:
        ok=False
        f1=i
    if s[i]=='Z': f2=i
print(f2-f1+1)