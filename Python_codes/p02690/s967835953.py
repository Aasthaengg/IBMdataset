X=int(input())
for i in range(-120,120):
    for j in range(max(i+1,1),120):
        if j**5-i**5==X:
            print(j,' ',i)
            exit()