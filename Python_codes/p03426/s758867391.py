h,w,d = map(int,input().split())
aij = [[int(i) for i in input().split()]for j in range(h)]
q = int(input())
lr = [[int(i) for i in input().split()]for j in range(q)]

pos = [0] * (h*w+1)

#print(pos)

for i in range(h*w):
    #print(i//h,i%w)
    #print(aij[i//w][i%w])
    pos[aij[i//w][i%w]] = [i//w,i%w]
    #pos.append([aij[i//h][i%w]])
 
#print(pos)
#exit()

rui = [0] * (h*w+1)
#print(pos[1])
tmp = 0

for j in range(d+1,h*w+1):
    #print(j,pos[j-d])
    rui[j] = rui[j-d] + abs(pos[j][0] - pos[j-d][0]) + abs(pos[j][1] - pos[j-d][1])
    """
    if j + d <= h*w:
        tmp += abs(pos[j][0] - pos[j+d][0]) + abs(pos[j][1] - pos[j+d][1])
        rui.append(tmp)
    else:
        break
    #pos[i][0])
    #rui.append()
    """
for i in range(q):
    print(rui[lr[i][1]]-rui[lr[i][0]])