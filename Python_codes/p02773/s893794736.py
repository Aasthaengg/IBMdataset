from collections import Counter
k = [input() for _ in range(int(input()))]
l = Counter(k)
m = l[max(l , key = lambda x: l[x])]
ans = sorted(filter(lambda x:l[x]==m ,l))
print(*ans, sep='\n')