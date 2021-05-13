from collections import Counter
n = int(input())
a = list(map(int, input().split()))
l = [i + a[i] for i in range(n)]
r = [i - a[i] for i in range(n)]
countl = Counter(l)
countr = Counter(r)
ans = sum([countl[i]*countr[i] for i in countl.keys()])
print(ans)