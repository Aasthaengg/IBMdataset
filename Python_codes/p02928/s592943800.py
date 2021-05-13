# A内で完結するものと、連結したときに変わるものがある
#
# 3 4 2 1 2 -> 3+3+1+0+0 = 7
# 3 4 2 1 2 | 3 4 2 1 2 -> (3*2)+(1*1+3*2)+(1*2)+0+(1*1) + 7 = 16 + 7
# 3 4 2 1 2 | 3 4 2 1 2 | 3 4 2 1 2 -> (3*3)+(2*1+3*3)+(1*3)+0+(2*1) + 16+7 = 25+16+7
# Aについて、i<jなるjでAi>Ajになるものがk個、Ai<Ajになるものがk-1個ある
# k=3で考えると
# 順方向: (m*3)+(m*3)+(m*1)+(0)+(0), m=1~3 = 7+14+21=42
# 逆方向：(0)+(m*1)+(0)+(0)+(m*1), m=1~2 = 2+4=6 （逆方向はk-1個）
# 合わせて48となりこれは上記で試してたのと等しい
# ということで、それぞれ等差数列の和が使えそう
n, k = map(int, input().split())
a = list(map(int, input().split()))
mod = 10**9 + 7

# 順方向
base = 0
for i in range(n):
    for j in range(i, n):
        if a[i] > a[j]:
            base += 1
# 逆方向
additional = 0
for i in range(n):
    for j in range(i):
        if a[i] > a[j]:
            additional += 1

ans = (k * (k + 1) // 2 % mod * base +
       (k - 1) * k // 2 % mod * additional) % mod
print(ans)
