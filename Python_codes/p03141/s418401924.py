N = int(input())

AB_list = [[0,0,0] for i in range(N)]

for i in range(N):
    a,b = map(int,input().split())
    AB_list[i][0] = a
    AB_list[i][1] = b
    AB_list[i][2] = a+b
AB_list.sort(reverse=True,key=lambda x:x[2])

total = 0
for i in range(N):
    if i%2==0:
        total += AB_list[i][0]
    else:
        total -= AB_list[i][1]

print(total)