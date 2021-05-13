import sys
#input=sys.stdin.read
adj=[[] for i in range(4)]
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))

for i in range(3):
    a,b=MAP()
    adj[a-1].append(b-1)
    adj[b-1].append(a-1)
for i in range(4):
    if len(adj[i])>2:
        print("NO")
        exit()
print("YES")
