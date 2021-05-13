array=[[0 for i in range(10)]for j in range(12)]
n=int(input())

for i in range(n):
    call=list(map(int,input().split()))
    array[(call[0]-1)*3-1+call[1]][call[2]-1]+=call[3]
for i in range(0,12):
    if i%3==0 and i!=0:
        for j in range(20):
            print("#",end="")
        print()
    for j in range(10):
        print(" "+str(array[i][j]),end="")
    print()