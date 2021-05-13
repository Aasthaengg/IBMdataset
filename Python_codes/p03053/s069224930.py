## coding: UTF-8


H,W = map(int,input().split())

c = []
for i in range(H):
    c.append(input())

fresh = [True] * (H*W)
#print(fresh)


queue = []
n = []
for i in range(H):
    for j in range(W):
        if(c[i][j] == '#'):
            fresh[i*W+j] = False
            queue.append(i*W+j)
#print('initial')
#print('fresh:{}'.format(fresh))
#print('queue:{}'.format(queue))

step = 0
status = True
while status:
    if(len(queue)>0):
        #処理を行う
        pivot = queue.pop()
        #print('pivot:{}, queue:{}, n:{}'.format(pivot, queue, n))        
        #右へ移動
        if(pivot%W != W-1 and fresh[pivot+1]):
            n.append(pivot+1)
            fresh[pivot+1] = False
        #左へ移動
        if(pivot%W != 0 and fresh[pivot-1]):
            n.append(pivot-1)
            fresh[pivot-1] = False
        #下へ移動
        if( int(pivot/W)<(H-1) and fresh[pivot+W]):
            n.append(pivot+W)
            fresh[pivot+W] = False
        #上へ移動
        if( int(pivot/W)>0 and fresh[pivot-W] ):
            n.append(pivot-W)
            fresh[pivot-W] = False
        #print('pivot:{}, queue:{}, n:{}'.format(pivot, queue, n))
    elif(len(n)>0):
        queue = n
        n = []
        #歩数を増やそう
        step += 1
        #print('step{}end,queue:{}, n:{}'.format(step, queue, n))
    else:
        status = False


print(step)
