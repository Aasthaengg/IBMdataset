S = input()
from collections import defaultdict
dic = defaultdict(int)
dic[0] += 1
# 後ろから見たほうがいい？
S = S[::-1]
d = 1
now = 0
for i in range(len(S)):
    # 2019で割ったあまりで集計する
    now += d*int(S[i]) % 2019
    dic[now%2019] += 1
    d *= 10
    d %= 2019
ans = 0
for k,v in dic.items():
    ans += v*(v-1)//2
print(ans)
