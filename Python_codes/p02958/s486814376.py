n = int(input())
p = list(map(int, input().split()))
q = sorted(p)
cnt = 0
for i in range(n):
    if p[i] != q[i]:
        cnt += 1
if cnt == 0 or cnt == 2:
    print("YES")
else:
    print("NO")