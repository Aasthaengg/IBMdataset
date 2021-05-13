n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
diff_po = [0]*n
diff_ne = 0
ans = 0
for i in range(n):
    num = a[i]-b[i]
    if num >= 0:
        diff_po[i] = num
    else:
        diff_ne += num
        ans += 1
diff_ne = -diff_ne
if sum(diff_po) < diff_ne:
    print(-1)
    exit()

if diff_ne == 0:
    print(0)
    exit()

diff_po.sort(reverse=1)
for i in diff_po:
    ans += 1
    diff_ne -= i
    if diff_ne <= 0:
        print(ans)
        break