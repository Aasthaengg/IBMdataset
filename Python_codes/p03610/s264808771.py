s=input()
a=s[0]
if len(s)%2==1:
    for i in range(1,(len(s)//2)+1):
        a+=s[2*i]
else:
    for i in range(1,(len(s)//2)):
        a+=s[2*i]
print(a)