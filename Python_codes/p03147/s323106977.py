# 問題文、rとlは固定かと思ったけど毎回指定するってのがサンプルから分かった
# 操作逆にしてぜんぶ0にするまでを数える
# NもHも小さいので「山になっている部分を減らす」を毎回やっても大丈夫だと思う
# しゃくとり的にやったけどちょっと雑
n = int(input())
h = list(map(int, input().split()))
ans = 0
s = sum(h)
while s > 0:
    left = 0
    while left < n and h[left] == 0:
        left += 1
    h[left] -= 1
    s -= 1
    right = left + 1
    while right < n and h[right] != 0:
        h[right] -= 1
        s -= 1
        right += 1
    ans += 1
print(ans)