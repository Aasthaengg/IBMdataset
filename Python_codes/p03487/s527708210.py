import collections
dic = collections.defaultdict(int)
n = int(input())
a = [int(i) for i in input().split()]
for i in range(n):
	dic[a[i]] += 1
ans = 0
for key in dic.keys():
    if dic[key] >= key:
    	ans += (dic[key] - key)
    else:
        ans += dic[key]
print(ans)
