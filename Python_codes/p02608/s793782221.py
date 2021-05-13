N=int(input())
li=[0]*N
for x in range(1,101):
    for y in range(1,101):
        for z in range(1,101):
            temp=x**2+y**2+z**2+x*y+y*z+z*x
            if temp<=N:
                li[temp-1]+=1
for i in range(N):
    print(li[i])
