from collections import defaultdict
N = int(input())
a = list(map(int,input().split()))
dic = defaultdict(int)
for x in a:
    dic[x] += 1
ans = 0
for x,c in dic.items():
    if c < x:
        ans += c
    elif c > x:
        ans += c-x
print(ans)