s = input()
n = len(s)
a1 = [0] * (n+1) # 左側に連続する<の個数
a2 = [0] * (n+1) # 右側に連続する>の個数
tmp1 = 0
tmp2 = 0
for i in range(n):
    if s[i] == "<": tmp1 += 1
    else: tmp1 = 0
    if s[n-i-1] == ">": tmp2 += 1
    else: tmp2 = 0
    a1[i+1] = tmp1
    a2[n-i-1] = tmp2
ans = 0
for i in range(n+1):
    ans += max(a1[i], a2[i])
print(ans)