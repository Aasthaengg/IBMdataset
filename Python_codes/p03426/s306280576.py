h,w,d = map(int,input().split())
adr = [-1]*(h*w) #indexの数字は[i,j]に書かれている
for i in range(h):
    a = list(map(int,input().split()))
    for j in range(w):
        adr[a[j]-1] = [i,j]
        
cost = [0]*(h*w)
for i in range(d,h*w):
    cost[i] = cost[i-d] + abs(adr[i][0]-adr[i-d][0]) + abs(adr[i][1]-adr[i-d][1])
        
q = int(input())
ans = []
for i in range(q):
    l,r = map(int,input().split())
    ans.append(cost[r-1]-cost[l-1])

for i in ans:
    print(i)