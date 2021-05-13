_ = input()
h = list(map(int, input().split()))
ans = 0
while sum(h) > 0:
    left = 0
    while left < len(h) and h[left] == 0:
        left += 1
    h[left] -= 1
    right = left + 1
    while right < len(h) and h[right] != 0:
        h[right] -= 1
        right += 1
    ans += 1
print(ans)

# 問題文、rとlは固定かと思ったけど毎回指定するってのがサンプルから分かった
# 操作逆にしてぜんぶ0にするまでを数える
# NもHも小さいので「山になっている部分を減らす」を毎回やっても大丈夫だと思う
# しゃくとり的にやったけどちょっと雑
# むしろこれでも間に合うか（毎回sumするver）