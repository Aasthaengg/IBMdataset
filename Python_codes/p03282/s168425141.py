s=(input())
k=int(input())
flag=1
for i in range(k):
    if(s[i]!='1'):
        print(s[i])
        flag=0
        break

if(flag==1):
    print("1")

