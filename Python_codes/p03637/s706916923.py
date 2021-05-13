a = int(input())
list = list(map(int, input().split()))

m=[0]*3
for i in list:
    if i%4==0:
        m[0]+=1
    elif i%2==0:
        m[1]+=1
    else:
        m[2]+=1

if(m[0]+1>=m[2]+m[1]%2):
    print("Yes")
else:
    print("No")
