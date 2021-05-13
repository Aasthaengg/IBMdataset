import sys
input = sys.stdin.readline

N, M = map(int, input().split())
L = [int(v) for v in input().split()]
L.sort()

s = sum(L)
d = set()
for i in range(1, int(s ** 0.5) + 1):
    if s % i == 0:
        d.add(i)
        d.add(s // i)
        
d = list(d)
d.sort(reverse = True)

ans = 1
for n in d:
    p = [v % n for v in L]
    p.sort()
    pc = n * N - sum(p)
    mc = 0
    for v in p:
        pc -= (n - v)
        mc += v
        
        if pc == mc:
            break
                
    if pc <= M:
        ans = max(ans, n)

print(ans)