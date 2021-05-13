N = int(input())
L = [[int(i) for i in input().split()] for i in range(N)]

ans = 0
for n in L:
    ans += n[1] - n[0] + 1

print(ans)