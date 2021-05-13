n, m = map(int, input().split())
load = []
for _ in range(m):
	load.extend(map(int, input().split()))

for i in range(n):
    print(load.count(i+1))
