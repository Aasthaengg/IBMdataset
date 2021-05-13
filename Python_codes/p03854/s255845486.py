s=input()
x=["eraser","erase","dreamer","dream",]
t=[]
flag=0
for i in range(4):
    if x[i] in s:
        s=s.replace(x[i],"1")
S=len(s)

for j in range(S) :
    if s[j]!="1":
        print("NO")
        flag+=1
        break

if flag==0:
    print("YES")