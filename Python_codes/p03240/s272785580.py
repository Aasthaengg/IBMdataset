n=int(input())
data=[]
for i in range(n):
    X,Y,H=map(int,input().split())
    data.append([H,X,Y])
data.sort(reverse=True)
for i in range(101):
    for j in range(101):
        H=abs(data[0][1]-i)+abs(data[0][2]-j)+data[0][0]
        for k in range(1,n):
            if max(H-abs(data[k][1]-i)-abs(data[k][2]-j),0)==data[k][0]:
                continue
            else:
                break
        else:
            print(str(i), str(j), str(H))

