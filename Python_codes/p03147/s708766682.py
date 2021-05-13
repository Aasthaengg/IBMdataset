N = int(input())
H = list(map(int,input().split()))

A = [[0]*N for _ in range(101)]
#A = [[0 for i in range(N)] for j in range(101)]
for i in range(101):
    for j in range(N):
        if H[j] > 0:
            A[i][j]=1
            H[j]-=1
        else:
            H[j] = 0
ans = 0
for i in range(101):
    flag = False
    for j in range(N):
        if A[i][j] == 1 and flag == False:
            flag = True
        elif A[i][j] == 0 and flag == True:
            ans += 1
            flag = False
    if flag:
        ans+=1
print(ans) 
