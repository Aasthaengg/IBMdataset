import sys
input = sys.stdin.readline
N = int(input())
D = [list(map(int, input().split())) for _ in range(N)]
result = 'No'
count = 0
for i in range(N):
    if D[i][0] == D[i][1]:
        count += 1
        if count == 3:
            result = 'Yes'
            break
    else:
        count = 0

print (result)

