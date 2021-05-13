n,m = map(int,input().split())
lst = [[] for i in range(n)]
for _ in range(m):
    a,b = map(int,input().split())
    lst[a-1].append(b-1)
    lst[b-1].append(a-1)

for v in lst:
    print(len(v))