N = int(input())
a = [int(x) for x in input().split()]

n4 = 0  # 4の倍数の個数
nodd = 0 # 奇数の個数
for i in range(N):
    nodd += (a[i] % 2 == 1)
    n4 += (a[i] % 4 == 0)

ans = "Yes"
if nodd > (N + 1) // 2:
    ans = "No"
elif n4 < min(nodd, N // 2):
    ans = "No"

print(ans)