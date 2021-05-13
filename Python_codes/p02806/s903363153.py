N = int(input())
S = [input().split() for i in range(N)]
X = input()
ans = 0

for j in range(N):
    if(X == S[j][0]):
        for k in range(j+1, N):
            ans += int(S[k][1])
        print(ans)
        exit()