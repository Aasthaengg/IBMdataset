c = [[0]*10 for _ in range(10)]

n = int(input())

for i in range(1,n+1):
    si = str(i)
    c[int(si[0])][int(si[-1])] += 1

ans = 0
for i in range(10):
    for j in range(10):
        ans += c[i][j]*c[j][i]

print(ans)