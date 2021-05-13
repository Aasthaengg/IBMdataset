n=int(input())

for i in range(n) :
    temp=1000*(i+1)-n
    if  temp>= 0 :
        print(temp)
        break