n = int(input())

if n <= 104:
    print(0)
    exit()
else:
    res = 0
    for i in range(105,n+1,2):
        temp = 0
        for j in range(1,i+1):
            if i %j ==0:
                temp+=1
        if temp==8:
            res+=1
print(res)