N,H,W = map(int, input().split(' '))
AB = [(input()) for i in range(N) ]
A = [int(AB[i].split()[0]) for i in range(N)]
B = [int(AB[i].split()[1]) for i in range(N)]

ans = 0
for i in range(N):
    if A[i] >= H:
        if B[i] >= W:
            ans +=1
            
print(ans)