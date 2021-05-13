n=int(input())
happines=[list(map(int,input().split())) for _ in range(n)]

solution=[[0,0,0] for _ in range(n)]

solution[0][0]=happines[0][0]
solution[0][1]=happines[0][1]
solution[0][2]=happines[0][2]

for i in range(1,n):
    for j in range(3):
        solution[i][j]=happines[i][j]+max(solution[i-1][(j+1)%3],solution[i-1][(j+2)%3])

print(max(solution[-1]))