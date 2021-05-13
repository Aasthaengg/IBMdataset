a,b,c,d=map(int,input().split())

flag=0

for i in range(101):
    if c-b*i<=0:
        print("Yes")
        flag+=1
        break
    
    elif flag==0:
        if a-d*i<=0:
            print("No")
            break
