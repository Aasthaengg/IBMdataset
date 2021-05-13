n, k = map(int, input().split())
maxim = (n-2) * (n-1) // 2
if k > maxim:
    print(-1)
    exit()

edges = [[x for x in range(n) if x > i] for i in range(n)]
count = 0
node = n-1
while count != k:
    if len(edges[node]) == 0:
        node -= 1
    edges[node].pop()
    count += 1

m = n * (n-1) // 2 - k
print(m)
for _from in range(n-1):
    for to in edges[_from]:
        print(_from+1, to+1)