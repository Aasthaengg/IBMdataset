s=input()

for i in range(len(s)-6):
    for j in range(len(s)-i+1):
        p=s[:j]+s[j+i:]
        if p=="keyence":
            print("YES")
            exit()
print("NO")