N=int(input())
count = 0
count2 = 0
for i in range(1,N+1):
    #print(i,"i")
    for j in range(1,N+1):
        #print(j,"k")
        if i % j == 0 :
            count += 1
            #print(count,"count")
    if count == 8 and i%2 != 0:
        count2 += 1
    ans = count2
    count = 0
print(ans)
