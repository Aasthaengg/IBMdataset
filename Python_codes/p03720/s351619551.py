N, M = map(int, input().split(' '))

ans = []
for n in range(N):
    ans.append(0)

for m in range(M):
    a,b = map(int, input().split(' '))
    ans[a-1] += 1
    ans[b-1] += 1

for a in ans:
    print(a)