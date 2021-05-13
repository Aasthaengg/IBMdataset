import math
x=int(input())

for i in range(x, x+100):
    cnt=0
    for j in range(2,int(math.sqrt(i))+1):
        if (i)%j==0:
            cnt+=1
            break
    if cnt==0:
        print(i)
        break