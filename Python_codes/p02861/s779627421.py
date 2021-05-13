N = int(input())
P = [list(map(int,input().split())) for i in range(N)]
ans = 0
for i in range(0,N-1):
    for j in range(i+1,N):
        ans += ((P[i][0]-P[j][0])**2 + (P[i][1]-P[j][1])**2)**(1/2)
print(ans*2/N)