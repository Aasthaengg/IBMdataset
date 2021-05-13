K = int(input())
if(K==0):
    print(4)
    print(3,3,3,3)
elif(K==1):
    print(3)
    print(1,0,3)
elif(K<50):
    n = K
    li = [i for i in range(n)]
    for i in range(n):
        for j in range(n):
            if(i==j):
                li[j] += n
            else:
                li[j] -= 1
    print(n)
    print(*li)
else:
    x = K%50
    y = K//50
    li = [y+i for i in range(50)]
    for i in range(x):
        for j in range(50):
            if(i==j):
                li[j] += 50
            else:
                li[j] -= 1
    print(50)
    print(*li)
