import itertools 
n = int(input())
a = []
shogen =[]
for i in range(n):
    a.append(int(input()))
    temp = []
    for j in range(a[i]):
        x,y = map(int,input().split())
        temp.append([x,y])
        
    shogen.append(temp)

pattern = list(itertools.product([0,1], repeat = n))
result = 0

#print('a',a)
#print('shogen',shogen)
for i in range(len(pattern)):
    flg = True
    check = [-1 for _ in range(n)]
    #j人目について考える
    for j in range(n):
        #正直者のとき
        if pattern[i][j] == 1:
            #全ての証言について考える
            for k in range(a[j]):
                #checkが更新されていないとき
                if check[shogen[j][k][0]-1] == -1:
                    check[shogen[j][k][0]-1] = shogen[j][k][1]
                else:
                    if check[shogen[j][k][0]-1] != shogen[j][k][1]:
                        flg = False
                        #print('break') 
                        break


    for l in range(n):
        if (pattern[i][l] == 1 and check[l] == 0) or (pattern[i][l] == 0 and check[l] == 1):
            flg = False
            break

    if flg:
        #print('pattern',pattern[i])
        result = max(result, sum(pattern[i]))

print(result)



