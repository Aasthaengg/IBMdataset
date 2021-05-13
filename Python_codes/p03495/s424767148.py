n,k = map(int, input().split())
a = list(map(int, input().split()))
r = [0 for _ in range(n)]
for i in a:
    r[i-1] += 1
t = []
for i in r:
    if i:
        t.append(i)
t.sort()
print(sum(t[:len(t)-k]))