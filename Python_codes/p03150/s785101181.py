s=input()
n="keyence"
res=False
if s[:7]==n or s[-7:]==n:
    res=True
else:
    for i in range(7):
        if s[:i+1]+s[i-6:]==n:
            res=True
            break

x="YES" if res else "NO"
print(x)
