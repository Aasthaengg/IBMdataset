N, C = list(map(int,input().split()))

sushi_front = [0]
sushi_back = [0]
sushi_front2 = [0]
sushi_back2 = [0]
sushi = []

c= 0
d = 0
max_ = 0
max_2 = 0
for _ in range(N):
    sushi.append(list(map(int,input().split())))
    
    c += sushi[-1][1]
    d = sushi[-1][0]
    max_ = max(max_,c-d)
    max_2 = max(max_2, c-2*d)
    sushi_front.append(max_)
    sushi_front2.append(max_2)

sushi.reverse()
c = 0
d = 0
max_ = 0
max_2 = 0
for x in sushi:
    
    c += x[1]
    d = C -x[0]
    max_ = max(max_,c-d)
    max_2 = max(max_2, c-2*d)
    sushi_back.append(max_)
    sushi_back2.append(max_2)

ans = 0
for i in range(N+1):
    ans = max(ans,sushi_front[i]+sushi_back2[N-i],sushi_front2[i]+sushi_back[N-i])
print(ans)