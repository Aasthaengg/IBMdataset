N = int(input())
k = []
for i in range(N):
    a,b = map(int,input().split())
    k.append([a,b])
k.sort()
t = k[len(k)-1][0]
u = k[len(k)-1][1]
print(t+u)