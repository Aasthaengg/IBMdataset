s =input()
s2 = int(s)
n= int(s)%9
mn = 0
while s2:
    mn+=s2%10
    s2//=10
print(max(mn,(len(s)-1)*9+(int(s[0])-1)))