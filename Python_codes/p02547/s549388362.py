N = int(input())
D = []
for i in range(N):
    D.append(list(map(int,input().split())))
ans = 0
for i in range(N-2):
    if D[i][0]==D[i][1] and D[i+1][0]==D[i+1][1] and D[i+2][0] ==D[i+2][1]:
        ans = 1
if ans == 1:
    print("Yes")
else:
    print("No")