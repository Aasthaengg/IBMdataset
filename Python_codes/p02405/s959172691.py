x=[]
y=[]
count=0
while True:
    i,j=map(int,raw_input().split())
    if (i,j)==(0,0):
        break
    count+=1
    x.append(i)
    y.append(j)

cord_1='#.'*150
cord_2='.#'*150

for i in range(count):
    for j in range(x[i]):
        if j%2==0:
            print(cord_1[:y[i]])
        else:
            print(cord_2[:y[i]])
    print('')