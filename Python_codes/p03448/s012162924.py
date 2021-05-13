a = int(input())
b = int(input())
c = int(input())
x = int(input())

res = 0
for i in range(a+1):
    aa = 500*i
    for j in range(b+1):
        bb = 100*j
        for k in range(c+1):
            cc = 50*k
            if aa+ bb+ cc ==x:
                res +=1

print(res)