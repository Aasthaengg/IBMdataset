N = int(input())
arr = list(map(int, input().split()))
cnt = arr.count(0)
if cnt == N:
    print('Yes')
    exit()
if N % 3 != 0:
    print('No')
    exit()
if cnt == N//3 and len(set(arr)) == 2:
    print('Yes')
    exit()
from collections import defaultdict
d = defaultdict(int)
for i in arr:
    d[i] += 1
if len(d) != 3:
    print('No')
    exit()
check = []
for key in d.keys():
    check.append(key)
if d[check[0]] == d[check[1]] and d[check[1]] == d[check[2]] and d[check[2]] == d[check[0]] and check[0]^check[1]^check[2] == 0:
    print('Yes')
else:
    print('No')
