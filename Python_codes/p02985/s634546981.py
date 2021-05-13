from collections import deque
import sys
input = sys.stdin.readline

MOD = 1000000007

class Factorial():
    def __init__(self,n,mod):
        self.mod = mod
        self.factorial = [0 for _ in range(n+1)]
        self.inv = [0 for _ in range(n+1)]
        self.factorial[0] = 1
        self.inv[0] = 1
        for i in range(n):
            self.factorial[i+1] = self.factorial[i]*(i+1)%mod
            self.inv[i+1] = self.inv[i]*pow(i+1,mod-2,mod)%mod
    def comb(self,m,k):
        return self.factorial[m]*self.inv[k]*self.inv[m-k]%self.mod
    def fact(self,m):
        return self.factorial[m]
    def perm(self,m,k):
        return self.factorial[m]*self.inv[m-k]%self.mod
    def invfact(self,m):
        return self.inv[m]

N,K = map(int,input().split())

tree = [[] for _ in range(N)]

for _ in range(N-1):
    a,b = map(int,input().split())
    tree[a-1].append(b-1)
    tree[b-1].append(a-1)
    
visited = [0 for _ in range(N)]
visited[0] = 1
queue = deque([0])
ans = K

f = Factorial(K+1,MOD)

while queue:
    node = queue.popleft()
    count = 0
    for adj in tree[node]:
        if not visited[adj]:
            visited[adj] = 1
            queue.append(adj)
            count += 1
    if node==0:
        if K-1 < count:
            print(0)
            break
        ans *= f.perm(K-1,count)
    else:
        if K-2 < count:
            print(0)
            break
        ans *= f.perm(K-2,count)
    ans %= MOD
            
else:
    print(ans)