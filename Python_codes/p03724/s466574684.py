from collections import defaultdict
dic = defaultdict(int)
n, m = map(int, input().split())
for i in range(m):
    a, b = map(int, input().split())
    dic[a] += 1
    dic[b] += 1
if [value for value in dic.values() if value % 2 == 1]:
    print('NO')
else:
    print('YES')
    
