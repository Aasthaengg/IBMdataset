s=input()
n=len(s)
for i in range(n):
    tmp=s[:i]+s[i+n-7:]
    if tmp=="keyence":
        print("YES")
        exit()
print("NO")