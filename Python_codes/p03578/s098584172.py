from collections import Counter
input()
d = Counter(map(int,input().split()))
input()
t = Counter(map(int,input().split()))

#print(d)
#print(t)
print('YES' if all(ti in d and d[ti] >= tc for ti,tc in t.items()) else 'NO')
