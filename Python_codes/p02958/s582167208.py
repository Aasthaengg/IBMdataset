N = int(input())
p = list(map(int, input().split()))
q = [i + 1 for i in range(N)]

cnt = 0
for i in range(N):
    if p[i] != q[i]:
        cnt += 1

ok = cnt == 2 or cnt == 0

print("YES" if ok else "NO")
