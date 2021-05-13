s=input()
t=input()
if not len(t)-len(s)==1:
    print("No")
    exit()
for i in range(len(s)):
    if not s[i]==t[i]:
        print("No")
        exit()
print("Yes")