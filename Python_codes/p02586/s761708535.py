## coding: UTF-8


R,C,K = map(int,input().split())
rcv = []
for i in range(K):
    rcv.append(list(map(int,input().split())))

item = [0] * (R*C+1)
for i in range(K):
    index = (rcv[i][0] - 1) * C + (rcv[i][1] - 1) 
    #available[index] = True
    item[index] = rcv[i][2]

#print(item)



def solver(R,C,K):
    empty = []
    prev = []
    for i in range(C):
        empty.append([0] * 4)
        prev.append([0] * 4)
    
    for i in range(R):
        #print('prev', prev)
        now = []
        #ret = []
        zero = max(prev[0])
        now.append([zero, zero+item[i*C], 0, 0]) #一番左
        for j in range(1, C):
            index = i * C + j
            point = item[index]
            #print(i,j,index)
            ret = []
            left = now[-1]
            zero = max(left[0], max(prev[j])) #左からor上から
            ret.append(zero) #0
            one = max(zero + point, left[1]) #左からor上からきてアイテム取得 or 左から一個持った状態で拾わない
            two = max(left[1] + point, left[2])
            three = max(left[2] + point, left[3])
            ret.append(one)
            ret.append(two)
            ret.append(three)
            now.append(ret)
        prev = now
        #print(now)
    
    print(max(now[-1]))


solver(R,C,K)

