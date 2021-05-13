lst=[]
for i in range(3):
    a=map(int,input().split())
    for j in a:
        lst.append(j)
for i in range(lst[0]+1):
    a,d=i,lst[0]-i
    b=lst[3]-lst[0]+a
    c=lst[6]-lst[0]+a
    e=lst[1]-lst[0]+d
    f=lst[2]-lst[0]+d
    if lst[4]==b+e and lst[5]==b+f and lst[7]==c+e and lst[8]==c+f:
        print("Yes")
        exit()
print("No")