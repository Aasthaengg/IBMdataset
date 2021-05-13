n = int(input())
A = list(map(int, input().split()))
m = {}
ans = 0
for i in range(n):
    x = A[i] + i   #i番目と当該数字の和
    if x not in m:
        m[x] = 0   #和の属性値を0とする
    m[x] += 1      #和の属性値に１を足す
    if i - A[i] in m: #i番目と当該数字の差
        ans += m[i - A[i]] #差の位置に当たる属性値を答えに足す
print(ans)