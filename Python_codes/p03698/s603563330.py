s=list(input())
n=len(s)
l=list("abcdefghijklmnopqrstuvwxyz")
f=0
for i in range(26):
    if s.count(l[i])>=2:
        f=1
print("yes" if f==0 else "no")
