n=int(input())
s=0
for i in range(n):
    l=input().split()
    if(l[1]=='JPY'):
        s+=float(l[0])
    else:
        s+=float(l[0])*(380000)
print(s)
