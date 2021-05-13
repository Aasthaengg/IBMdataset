n,m = map(int,input().split())
# m の約数を求めるのです
i = 1
#import collections
#dic = collections.defaultdict(int)
li = []
while i*i <= m:
    if m % i == 0:
        if m//i != i:
            li.append(i)
            li.append(m//i)
        else:
            li.append(i)
    i += 1
#print(li)
# 最大の最大公倍数 N*d <= M
ans = 1
for v in li:
    if n*v <= m:
        ans = max(ans,v)
print(ans)
