n= int(input())
cont=0
yes=0
for x in range(n):
    a,b= input().split()
    a, b= int(a), int(b)
    if a==b:
        cont+=1
    else:
        cont=0
    if cont>=3:
        yes=1
if yes==1:
    print("Yes")
else:
    print("No")