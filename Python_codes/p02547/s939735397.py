N = int(input())
S = []
judge = 0
for i in range(N):
    S += [input().split()]
for i in range(N):
    if i <= N-3:
        if S[i][0] == S[i][1]:
            if S[i+1][0] == S[i+1][1]:
                if S[i+2][0] == S[i+2][1]:
                    print("Yes")
                    judge = 1
                    break
if judge == 0:
    print("No")
