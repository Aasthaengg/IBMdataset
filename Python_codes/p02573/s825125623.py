import queue
N, M = map(int, input().split())
l = [[] for i in range(N)]
for i in range(M):
        a, b = map(int, input().split())
        l[a - 1].append(b - 1)
        l[b - 1].append(a - 1)
c = [0] * N 
ans = 1
q = queue.Queue()
for j in range(N):
        q.put(l[j])
        u = 0 
        while not q.empty():
                temp = q.get()
                for k in temp:
                        if c[k]:
                                continue
                        c[k] = 1 
                        u += 1
                        q.put(l[k])
        ans = max(ans, u)
print(ans) 