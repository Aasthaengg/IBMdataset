N = int(input())
a = [int(i) for i in input().split()]

ans = 0
flg = False
for i in range(1, N):
    if flg is False and a[i] == a[i-1]:
        ans += 1
        flg = True
    else:
        flg = False
print(ans)
