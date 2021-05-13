N = int(input())
ab = []
for _ in range(N):
    tmp = list(map(int, input().split()))
    ab.append(tmp)

ans = 0
for i in reversed(range(N)):
    if (ab[i][0]+ans) % ab[i][1] != 0:
        a = (ab[i][0]+ans)
        b = ((ab[i][0]+ans)//ab[i][1]+1)*ab[i][1]
        ans += abs(a-b)
print(ans)
