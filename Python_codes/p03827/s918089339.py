n=int(input())
s=input()
x=0
L=[0]
for i in range(n):
    if s[i]=="I":
        x+=1
    elif s[i]=="D":
        x-=1
    L.append(x)
print(max(L))