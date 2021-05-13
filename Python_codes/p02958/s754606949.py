n = int(input())
p = list(map(int, input().split()))
a = [i for i in range(1, n+1)]
cnt = 0
for j in range(n):
    if p[j] != a[j]:
        cnt += 1
if cnt <= 2:
    print("YES")
else:
    print("NO")