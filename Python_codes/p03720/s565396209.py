n,m = map(int, input().split()) 
AB = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int,input().split())
    a -= 1
    b -= 1 
    AB[a].append(b)
    AB[b].append(a)

for i in range(n):
    print(len(AB[i]))
