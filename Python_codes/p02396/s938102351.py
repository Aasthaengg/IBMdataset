num = []
count = 0
while True:
    x = int(input())
    if x ==0:
        break
    num.append(x)
    count +=1
for i,j in zip(range(1,count+1),num):
    print('Case '+str(i)+': '+str(j))