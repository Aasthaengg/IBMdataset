# やるだけ
n = int(input())
a = list(map(int, input().split()))
d = {}
for i in range(n):
    if a[i] not in d:
        d[a[i]] = 1
    else:
        d[a[i]] += 1
ans = 0
for k, v in d.items():
    if k > v:
        # そもそも足りない場合はまるごとなかったことにしなければいけない（増やせないので
        ans += v
    elif k < v:
        # 多かった場合は差分
        ans += v - k
print(ans)