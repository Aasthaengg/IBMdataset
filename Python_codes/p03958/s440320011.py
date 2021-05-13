K, T = map(int, input().split())
a = sorted(list(map(int, input().split())))[::-1]
ans = a[0]-1

for i in range(1, T):
    ans -= a[i]
    if ans < 0:
        print(0)
        exit()
print(ans)