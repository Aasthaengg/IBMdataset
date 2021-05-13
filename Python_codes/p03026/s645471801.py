from collections import deque, _heapq
N = int(input())

g = [{"num":0, "neighber":[]} for _ in range(N+1)]

for _ in range(N-1):
    x, y = map(int, input().split())
    g[x]["neighber"].append(y)
    g[y]["neighber"].append(x)

c = sorted(map(int, input().split()))
print(sum(c[:-1]))

i = 0
s = [(0, 1)]
while i < len(s):
    pre, cur = s[i]
    i+=1
    g[cur]["num"] = c.pop()

    for x in g[cur]["neighber"]:
        if x == pre:
            continue
        s.append((cur, x))

print(" ".join((str(g[i]["num"]) for i in range(1, N+1))))
