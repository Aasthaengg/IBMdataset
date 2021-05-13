a, b = map(int,input().split())
a_list = []
b_list = []
flag = 0

for i in range(1,1009):
    if int(i*1.08)-i == a:
        a_list.append(i)

for j in a_list:
    if int(j*1.1)-j == b:
        print(j)
        flag = 1
        break

if flag != 1:
    print('-1')
