n = int(input())
a = list(map(int,input().split()))

ans = 0
c = 0
tmp_m = 10**9
zero = False
for i in range(n):
    if a[i] < 0:
        c += 1
    elif a[i] == 0:
        zero = True
    tmp = abs(a[i])
    ans += tmp
    tmp_m = min(tmp_m,tmp)

if zero:
    print(ans)
else:
    if c%2 == 0:
        print(ans)
    else:
        print(ans-tmp_m*2)
