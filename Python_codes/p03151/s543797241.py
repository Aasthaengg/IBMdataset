n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
s_a = sum(a)
s_b = sum(b)
if s_b > s_a:
    print(-1)
    exit()
dist_s = s_a - s_b
dist_list = []
for i in range(n):
    if a[i] >= b[i]:
        dist_list.append(a[i]-b[i])
dist_list.sort()
m = len(dist_list)
count = 0
ans = n
while dist_s > 0 and count < m:
    dist_s -= dist_list[count]
    ans -= 1
    count += 1
    if dist_s < 0:
        ans += 1
print(ans)