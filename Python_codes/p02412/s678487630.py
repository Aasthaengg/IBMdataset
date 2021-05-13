x=1
y=1
list=[]
while x>0:
    if x ==0 and y == 0:
        break
    x,y = map(int,input().split())
    list.append([x,y])

list.remove([0,0])

for L in list:
    ans = 0
    for i in range(1,L[0]-1):
        for j in range(i+1,L[0]):
            for k in range(j+1,L[0]+1):
                if L[1]== i + j+ k:
                    ans += 1
                else:
                    pass
    print(ans)