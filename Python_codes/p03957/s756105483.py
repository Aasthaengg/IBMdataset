s=list(input())
c=False
for x in s:
    if not c:
        if x=="C":c=True
    if c and x=="F":
        print("Yes")
        exit(0)
print("No")