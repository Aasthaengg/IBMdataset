x=a=b=c=0
for _ in "_"*int(input()):s=input();x+=s.count("AB");a+=s[-1]=="A";b+=s[0]=="B";c+=(s[0]+s[-1])=="BA"
print(x+min(a,b)-(0<a==b==c))