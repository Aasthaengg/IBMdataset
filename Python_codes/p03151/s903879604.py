n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

excess = []
shortage = []

ans = 0

for i in range(n):
    if a[i] >= b[i]:
        excess.append(a[i] - b[i])
    else:
        shortage.append(b[i] - a[i])

ans = len(shortage)

if sum(excess) < sum(shortage):
    print(-1)
elif len(shortage) == 0:
    print(0)
else:
    excess.sort(reverse=True)
    excess_num = 0
    shortage_num = sum(shortage)
    for i in range(n):
        excess_num += excess[i]
        ans += 1
        if excess_num >= shortage_num:
            print(ans)
            exit()