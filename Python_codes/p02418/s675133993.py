s=input()
p=input()

s=s+s[:-1]

if s.find(p)!=-1:
    print("Yes")
else:
    print("No")
