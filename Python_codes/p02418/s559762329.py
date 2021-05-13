s=str(input())
p=str(input())
s+=s
if s.find(p)<0:
    print("No")
else:
    print('Yes')
