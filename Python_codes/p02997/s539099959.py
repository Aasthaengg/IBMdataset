import sys
N, K = map(int, input().split())
MAXP = (N - 1) * (N - 2) // 2
res = MAXP - K

if res < 0:
    print(-1)
    sys.exit()

M = (N - 1) + res

root = 2
end = root + 1

print(M)
for i in range(2,N+1):
    print(1, i)

for _ in range(res):
    if end > N:
        root += 1
        end = root + 1
    print(root, end)
    end += 1