import sys
input = sys.stdin.readline

N, K = map(int,input().split())
td = [list(map(int, input().split())) for _ in range(N)]
td.sort(key=lambda x: (x[0],x[1]),reverse=True)

x= []
y= []
y.append(td[0][1])
for i in range(1,N):
    if td[i][0] != td[i-1][0]:
        y.append(td[i][1])
    else:
        x.append(td[i][1])
x.sort(reverse=True)
y.sort(reverse=True)
ans = 0
sum_y = 0
sum_x = []
tmp = 0
sum_x.append(0)
for i in range(len(x)):
    tmp += x[i]
    sum_x.append(tmp)

for i in range(1,min(K,len(y))+1):
    sum_y += y[i-1]
    if len(sum_x) < K-i+1: continue
    ans = max(ans, sum_y + sum_x[K-i] + i*i)
    
print(ans)
