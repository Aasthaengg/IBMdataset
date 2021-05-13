a=b=c=ans=0
for _ in range(int(input())):
    s=input()
    ans+=s.count("AB")
    a+=s[-1]=="A"
    b+=s[0]=="B"
    c+=s[-1]+s[0]=="AB"
print(ans+min(a,b)-(0<a==b==c))
