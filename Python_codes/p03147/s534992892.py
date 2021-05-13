N = int(input())

h = [i for i in map(int, input().split())]

hmax = max(h)
hmin = min(h)


ans = hmin
for i in range(hmin+1, hmax+1):
    count = 0
    flag = False
    for j in h:
        if j < i and flag:
            flag = False
        elif j >= i and not flag:
            flag = True
            count += 1
    ans += count

print(ans)
