from collections import deque

H,W = list(map(int,input().split()))
D_h = {}
D_w = {}

for h in range(H):
    D_h[h]=deque([-1])
    
for w in range(W):
    D_w[w]=deque([-1])
    
for h in range(H):
    D = list(input())
    for w in range(W):
        if D[w] =='#':
            D_h[h].append(w)
            D_w[w].append(h)
            
    D_h[h].append(W)
    
for w in range(W):
    D_w[w].append(H)
    
Lamp_h = [ [0] * W  for h in range(H) ]

for d_h in D_h.keys():
    obst = D_h[d_h]
    for o_ed in range(1,len(obst)):
        o_st = o_ed-1
        
        o_st = obst[o_st]
        o_ed = obst[o_ed]
        
        for o in range(o_st+1,o_ed):
            Lamp_h[d_h][o] = o_ed-1 - o_st
    
Lamp_w =  [ [0] * H  for w in range(W) ]
for d_w in D_w.keys():
    obst = D_w[d_w]
    for o_ed in range(1,len(obst)):
        o_st = o_ed-1
        
        o_st = obst[o_st]
        o_ed = obst[o_ed]
        
        for o in range(o_st+1,o_ed):
            Lamp_w[d_w][o] = o_ed-1 - o_st
    
ans = 0
for h in range(H):
    for w in range(W):
        ans_ = Lamp_h[h][w] + Lamp_w[w][h] 
        if ans < ans_:
            ans =ans_
        
print(ans-1)