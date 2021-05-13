from operator import itemgetter
N, M = map(int, input().split())
AB = [tuple(map(int, input().split())) for _ in range(N)]
AB.sort(key=itemgetter(0))
ans = 0
for i in range(N):
    ans += min(M, AB[i][1]) * AB[i][0]
    M -= min(M, AB[i][1])
    if M==0:
        break
print(ans)
