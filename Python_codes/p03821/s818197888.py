N = int(input())
AB = [[int(hoge) for hoge in input().split()] for j in range(N)]

ans = 0
for a,b in reversed(AB):
    a += ans
    ans += -a % b
print(ans)