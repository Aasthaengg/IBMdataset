s=input()
n=len(s)
c=0

if n%2==1:
    for i in range((n-1)//2):
        if s[i]!=s[-i-1]:
            c+=1
else:
    for i in range(n//2):
        if s[i]!=s[-i-1]:
            c+=1
print(c)