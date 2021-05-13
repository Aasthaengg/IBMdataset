date=[]
while True:
    x, y= [int(i) for i in input().split()]
    count=0
    if x == 0 and y ==0:
        break
    else:
        for k in range(1,x-1):
            for h in range(k+1,x):
                for g in range(h+1,x+1):
                    if k + h + g == y:
                        count = count + 1
    date.append(count)

for u in range(0,len(date)):
    print(date[u])