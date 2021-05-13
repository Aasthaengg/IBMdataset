N = int(input())
T = [[0,0,0]]+[ [int(x) for x in input().split()] for _ in range(N)]

flag = 'Yes'
i = 0
while flag=='Yes' and i<len(T)-1:
    t1,x1,y1 = T[i] 
    t2,x2,y2 = T[i+1]
    dis = abs(x2-x1)+abs(y2-y1)
    _t = t2-t1
    if dis > _t or _t%2 != dis%2:
        flag = 'No'
    i += 1        
print(flag)