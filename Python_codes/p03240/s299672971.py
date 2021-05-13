n=int(input())
data=[]
for i in range(n):
    data.append(list(map(int,input().split())))
    
first_h_index=0
for i in range(n):
    if data[i][2] > 0:
        first_h_index=i
        break
    
for i in range(101):
    for j in range(101):
        h=data[first_h_index][2]+abs(data[first_h_index][0]-i)+abs(data[first_h_index][1]-j)
        for k in range(n):
            if data[k][2] != max(h-abs(data[k][0]-i)-abs(data[k][1]-j),0):
                break
        else:
            print(i,j,h)
            break