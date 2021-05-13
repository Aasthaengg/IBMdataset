from collections import Counter
N, M = map(int, input().split())
node = []
for i in range(M):
    a, b = map(int, input().split())
    a, b = a-1, b-1
    node.append(a)
    node.append(b)
C = Counter(node)
ret = 'YES'
for c in C.values():
    if c % 2 == 1:
        ret = 'NO'
        break
print(ret)