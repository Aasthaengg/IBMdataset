N = int(input())
p = list(map(int, input().split()))
p2 = sorted(p)
cnt = 0
for i in range(N):
    if p[i] != p2[i]:
        cnt += 1
if cnt == 0 or cnt == 2:
    print("YES")
else:
    print("NO")
