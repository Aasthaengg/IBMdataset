N = int(input())
T = list(map(int, input().split()))
s = sum(T)
M = int(input())
res = [0] * M
for i in range(M):
    p, x = map(int, input().split())
    res[i] = s - T[p-1] + x
print(*res, sep='\n')