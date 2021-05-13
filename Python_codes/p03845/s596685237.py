N = int(input())
T = list(map(int, input().split()))
M = int(input())

ans = []

for m in range(M):
    tmp = T[:]
    p, x = map(int, input().split())
    tmp[p-1] = x
    ans.append(sum(tmp))

print(*ans, sep="\n")