from collections import Counter
n, k = map(int, input().split())
a = list(map(int, input().split()))
syurui = len(set(a))
#print(syurui)
c = Counter(a)
ans = 0
c_sort = c.most_common()
#print(c_sort)
for i in range(1, syurui-k + 1):
    ans += c_sort[-i][1]
print(ans)