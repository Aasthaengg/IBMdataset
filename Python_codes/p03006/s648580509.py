from collections import deque
def solve():
    N = int(input())
    X = [0]*N
    Y = [0]*N
    balls = [0]*N
    ans = N
    dic = {}
    f = {}
    for i in range(N):
        X[i],Y[i] = map(int, input().split())
        dic[(X[i],Y[i])] = i
        balls[i] = [X[i],Y[i]]
    
    balls = sorted(balls, key=lambda x:(x[0],x[1]))

    for x1, y1 in zip(X,Y):
        for x2, y2 in zip(X,Y):
            p = x2 - x1
            q = y2 - y1
            if p == 0 and q == 0:
                continue
            collected = [False]*N
            collected[dic[(x1,y1)]]=True
            collected[dic[(x2,y2)]]=True
            d = deque(balls)
            cnt = 1
            x = x2 + p
            y = y2 + q
            while (x,y) in dic:
                collected[dic[(x,y)]] = True
                x += p
                y += q
            while len(d)>0: 
                if p<0 or p==0 and q<0:
                    x,y = d.pop()
                else:
                    x,y = d.popleft()
                if collected[dic[(x,y)]] == True:
                    continue
                cnt += 1
                while (x,y) in dic:
                    collected[dic[(x,y)]] = True
                    x += p
                    y += q
            ans = min(ans, cnt)
    return ans
print(solve())