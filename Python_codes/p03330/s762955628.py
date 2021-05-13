import itertools
n,c = map(int,input().split())
dij = [[int(i) for i in input().split()] for j in range(c)]
cij = [[int(i) for i in input().split()] for j in range(n)]

c0 = []
c1 = []
c2 = []


for i in range(1,c+1):
    c0_tmp = 0
    c1_tmp = 0
    c2_tmp = 0
    for j in range(n*n):
        c_num = cij[j//n][j%n]
        cnt = j//n + j % n + 2
        if cnt % 3 == 0:
            if c_num != i:
                #print(i,c_num,j)
                c0_tmp += dij[c_num-1][i-1]
        elif cnt % 3 == 1:
            if c_num != i:
                c1_tmp += dij[c_num-1][i-1]
            #c1.append(j+2)
        else:
            if c_num != i:
                c2_tmp += dij[c_num-1][i-1]
            #c2.append(j+2)
    c0.append(c0_tmp)
    c1.append(c1_tmp)
    c2.append(c2_tmp)
        
li = list(itertools.permutations(range(1, c+1),3))

ans = 10**18

for i in range(len(li)):
    tmp = 0
    #print(li[i])
    tmp += c0[li[i][0]-1]
    tmp += c1[li[i][1]-1]
    tmp += c2[li[i][2]-1]
    #print(tmp,i)
    #print(li[i][0])
    ans = min(ans,tmp)

print(ans)