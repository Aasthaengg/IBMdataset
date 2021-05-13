s=input()
n=len(s)
tmp=0
for i in range(n):
    if s[i]!="o":
        tmp+=1
if tmp>7:
    print("NO")
else:
    print("YES")