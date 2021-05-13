import string
s=input()
n=len(s)
l=string.ascii_lowercase
if n<26:
    for c in l:
        if c not in s:
            print(s+c)
            exit()
elif s==l[::-1]:
    print(-1)
    exit()
else:
    for i in range(24,-1,-1):
        for j in range(25,i,-1):
            if s[i]<s[j]:
                print(s[:i]+s[j])
                exit()