n=int(input())
l=list()
flag=0
for i in range(1, 10):
    if n % i == 0: 
        if (n//i)<=9:
            flag+=1

if flag>0:
    print("Yes")
else:
    print("No")
