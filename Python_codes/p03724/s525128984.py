from collections import Counter

n, m = map(int, input().split())
graph = []
for _ in range(m):
    graph.extend([int(i) for i in input().split()])
    
cnt = Counter(graph)
ans = 'YES'
for i in cnt.values():
    if i % 2 != 0:
        ans = 'NO'
        break
print(ans)    