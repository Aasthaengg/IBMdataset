N = int(input())
H = [[0,0,0] for i in range(N)]
H[0] = list(map(int, input().split()))
for i in range(1, N):
    abc = list(map(int, input().split()))
    for j in range(3):
        H[i][j] = max(H[i-1][j-1],H[i-1][(j+1)%3])+abc[j]

print(max(H[-1]))