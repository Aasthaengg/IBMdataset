List=[int(input()) for i in range(5)]
num=[10,20,30,40,50,60,70,80,90,100,110,120,130]
time=0
table=[]
for i in range(5):
    subtract=0
    for j in range(len(num)):
        if List[i]<=num[j]: 
            subtract=num[j]
            break
    table.append([subtract-List[i],List[i]])
table.sort()
for i in range(5):
    time+=table[i][0]+table[i][1]
time-=table[4][0]
print(time)