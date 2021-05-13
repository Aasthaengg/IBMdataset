n = int(input())
s_list = []

for i in range(n):
    x,y,h = map(int,input().split())
    s_list.append([x,y,h])

s_list.sort(key=lambda x: x[2])
s_list = list(reversed(s_list))

H = 0
flag = 0

for i in range(101):
    for j in range(101):
        flag = 0
        H = s_list[0][2] + abs(i-s_list[0][0]) + abs(j-s_list[0][1])
        for k in range(1,n):
            if s_list[k][2] != max(H - abs(s_list[k][0]-i) - abs(s_list[k][1]-j),0):
                flag = 1
                break
        if flag == 0:
            print(i,j,H)
            break
