n = int(input())

D = [] * n

for i in range(n):
    D.append(list(map(int, input().split())))

ans = 'No'

for i in range(0, n-2):
    if D[i][0] == D[i][1] and D[i+1][0] == D[i+1][1] and D[i+2][0] == D[i+2][1]:
        ans = 'Yes'
        break

print(ans)