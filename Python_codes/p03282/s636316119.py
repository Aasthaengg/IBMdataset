s=input()
k=int(input())
flag=True
i=0
while flag:
    if i==len(s):
        break
    elif s[i]!="1":
        res=s[i]
        flag=False
    else:
        i+=1
if k>i:
    print(res)
else:
    print(1)
