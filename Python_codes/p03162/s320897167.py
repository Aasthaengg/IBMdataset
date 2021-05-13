
n = int(input())
summmer = [""]*n
for i in range(n):
    summmer[i] = list(map(int,input().split()))
happy = [0]*(n+1)
for i in range(n+1):
    happy[i] = [0]*3
yesterday = -1
for i in range(1,n+1):
    happy[i][0] = max(happy[i-1][1] + summmer[i-1][0],happy[i-1][2] + summmer[i-1][0]) 
    happy[i][1] = max(happy[i-1][0] + summmer[i-1][1],happy[i-1][2] + summmer[i-1][1]) 
    happy[i][2] = max(happy[i-1][0] + summmer[i-1][2],happy[i-1][1] + summmer[i-1][2]) 
# print(happy)
print(max(happy[-1]))

