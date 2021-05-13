#同じ文字の間隔を2文字以上空ける　abcabcabc,,,,,
s=input()
if len(s)==1:
    print("YES")
    exit()
    
c=[0,0,0]
for i in range(len(s)):
    if s[i]=="a":
        c[0]+=1
    elif s[i]=="b":
        c[1]+=1
    elif s[i]=="c":
        c[2]+=1
if max(c)-min(c)>=2:
    print("NO")
else:
    print("YES")