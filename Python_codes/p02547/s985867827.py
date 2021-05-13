N = int(input())

cnt = 0
ans = 'No'

for _ in range(N):
    D = input().split()
    cnt = (cnt + 1)*(D[0] == D[1])
    if cnt == 3:
        ans = 'Yes'

print(ans)