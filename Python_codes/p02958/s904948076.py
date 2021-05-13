n = int(input())
p = list(map(int, input().split()))
cnt = 0

for i in range(0, n):
    if (i+1) != p[i]:
        cnt += 1

if cnt < 3:
    print("YES")
else:
    print("NO")