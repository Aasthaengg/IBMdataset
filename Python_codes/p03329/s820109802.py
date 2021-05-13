N=int(input())

#1*a+(6^b1)*b+(9^c1)*c
list=[99999]*(N+1)
list[0]=0
list[1]=1
#1回でいけるところをあらかじめ記入
max6end =True
i=0
while max6end:
    if N <= 6**i :
        max6=i
        max6end=False
    i+=1
max9end =True
i=0
while max9end:
    if N <= 9**i :
        max9=i
        max9end=False
    i+=1
    
#print ("max6=%d max9=%d" % (max6,max9))
for n in range(1,N+1):
    list[n]=list[n-1]+1
    for i in range(1,max6+1):
        if n < 6**i:
            break
        else:
            if list[n] >= list[n-6**i]+1:
                list[n]=list[n-6**i]+1
    for i in range(1,max9+1):
        if n < 9**i:
            break
        else:
            if list[n] >= list[n-9**i]+1:
                list[n]=list[n-9**i]+1
print(list[N])