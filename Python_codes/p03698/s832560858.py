s=list(input())
s.sort()
for i in range(len(s)):
    if s[i]==s[i-1]:
        print("no")
        exit()
print("yes")
