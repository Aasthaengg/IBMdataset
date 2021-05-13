n,m=map(int,input().split())
lista=[]
for i in range(n):
    lista.append(input())
listb=[]
for i in range(m):
    listb.append(input())
ans=0
num1=n-m+1
for i in range(num1):
    for j in range(num1):
        yn=0
        for k in range(m):
            str1=lista[i+k]
            if listb[k]!=str1[j:j+m]:
                yn=1
                break
        if yn==0:
            ans=1
            break
    if ans==1:
        break
if ans==0:
    print("No")
else:
    print("Yes")
