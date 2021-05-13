n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
b_a = [0] * n
for i in range(n):
    b_a[i] = a[i] - b[i]
b_a.sort()
total = sum([-1 * i for i in b_a if i < 0])  # 負の要素のsum * -1
lim = len([-1 * i for i in b_a if i < 0])  # 負の個数 3　なら0,1,2 が負
#print(b_a, total, lim)
num = 0
if total == 0:
    print(0)
    exit()
while total > 0:  # 全部正の時にtotal=0でここには入らなくて良い。
    total -= b_a[-num - 1]
    num += 1
    if num == n - 1:  # 無限るーぷしないように、n-num-1 がlim-1まできたらbreak
        print(-1)
        exit()
print(num + lim)
