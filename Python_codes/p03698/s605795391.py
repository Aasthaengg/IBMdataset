s=input()
s=sorted(s)
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        print("no")
        exit(0)
print("yes")