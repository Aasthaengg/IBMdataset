N = int(input())
res=[0 for _ in range(10050)]
for x in range(1,105):
    for y in range(1,105):
        for z in range(1,105):
            k=x*x+y*y+z*z+x*y+y*z+z*x
            if k<10050:
                res[k]+=1
for i in range(N):
    print(res[i+1])
