n = input()    
m = n.split()
p = [int(i) for i in m]
from collections import deque
list = []
for i in range(p[0]-1): #因数注意！
    n = input()    
    m = n.split()
    q = [int(i) for i in m] #1列の数列をリスト化
    list.append(q)
l = [[] for i in range(p[0]+1)]
for pi in list:  #0-originedに注意
    l[pi[0]].append(pi[1])
    l[pi[1]].append(pi[0])
sousa = deque([[p[2],0,0]]) #[捜査対象ノード,親ノード,そのノードの距離]
node = [[] for i in range(p[0])] #n番目のリストにn+1について[親ノード,rootからの距離,子ノード]
while len(sousa) != 0:
    a = sousa.popleft()
    b = l[a[0]]
    if a[1]!=0:
        b.remove(a[1])
    if len(b) == 0:
        pass
    else:
        for i in b:
            sousa.append([i,a[0],a[2]+1])
    node[a[0]-1] = [a[1]] + [a[2]] + b
dis = node[p[1]-1][1]
takahashi = p[1]
max = dis
hate = p[1]
for i in range((dis+1)//2):
    tansaku = deque([[takahashi,dis]])
    if i >= 1:
        kitatoko = takahashi
        takahashi = node[takahashi-1][0]
        a = tansaku.popleft()
        b = node[takahashi-1][2:]
        b.remove(kitatoko)
        if len(b) == 0:
            continue
        else:
            for j in b:
                tansaku.append([j,dis+1-i])

    while len(tansaku) != 0:
        a = tansaku.popleft()
        b = node[a[0]-1][2:]
        print()
        if len(b) == 0:
            pass
        else:
            for j in b:
                tansaku.append([j,a[1]+1])

    if max < a[1]:
        max = a[1]
        hate = a[0]
print(node[hate-1][1]-1)