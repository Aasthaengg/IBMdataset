r,c = map(int,input().split(' '))
arr = [[0 for i in range(c+1)] for i in range(r+1)]

for i in range(r):
    row = list(map(int,input().split(' ')))
    for j in range(c):
        arr[i][j] = row[j]

for i in range(r):
    for j in range(c):
        arr[i][-1] += arr[i][j]
for i in range(c):
    for j in range(r):
        arr[-1][i] += arr[j][i]
        
if c == 1:
    for i in range(r):
        arr[-1][-1] += arr[i][0]
elif r == 1:
    for i in range(c):
        arr[-1][-1] += arr[0][i]
else:
    for i in range(r):
        arr[-1][-1] += arr[i][-1]
    
for i in range(r+1):
    for j in range(c):
        print(arr[i][j],end = ' ')
    print(arr[i][-1])