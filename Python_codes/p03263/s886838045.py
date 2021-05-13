H,W = list(map(int,input().split()))

coin=[[0]*(W+2)]
for h in range(H):
    c=[0]
    c.extend(list(map(int,input().split())))
    c.append(0)
    coin.append(c)
coin.append([0]*(W+2))
    
position=[]
for h in range(1,H+1):
    W_list=list(range(1,W+1))
    if h % 2 == 0:
        W_list.reverse()
    for w in W_list:
        position.append([h,w])
        
ans=[]
for p1,p2 in zip(position[:-1],position[1:]):
    if coin[p1[0]][p1[1]] % 2 != 0:
        coin[p1[0]][p1[1]] -= 1
        coin[p2[0]][p2[1]] += 1
        ans.append([p1[0],p1[1],p2[0],p2[1]])
        
print(len(ans))
for a in ans:
    print(' '.join(map(str,a)))