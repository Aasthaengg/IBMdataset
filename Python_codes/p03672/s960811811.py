s=input()
for i in range(200):
    s=s[0:len(s)-1]
    if len(s)%2==1:
        continue
    if s[0:len(s)//2]*2==s:
        print(len(s))
        exit()