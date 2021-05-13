N = int(input())

table = ['x'] + ([0] * N)
for i in range(1,N+1):
    for j in range(i,N+1,i):
        table[j] += 1

ans = 0

for i in range(1,N+1,2):
    if table[i] == 8:
       ans += 1

print(ans)
