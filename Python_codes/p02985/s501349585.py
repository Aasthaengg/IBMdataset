from collections import deque
import bisect
import sys
sys.setrecursionlimit(10**9)

def mi(): return map(int,input().split())
def ii(): return int(input())
def isp(): return input().split()

class Counting():
    def __init__(self,maxim,mod):
        maxim += 1

        self.mod = mod
        self.fact = [0]*maxim
        self.fact[0] = 1
        for i in range(1,maxim):
            self.fact[i] = self.fact[i-1] * i % mod

        self.invfact = [0]*maxim
        self.invfact[maxim-1] = pow(self.fact[maxim-1],mod-2,mod)
        for i in reversed(range(maxim-1)):
            self.invfact[i] = self.invfact[i+1] * (i+1) % mod


    def nCk(self,n,r):
        if n < 0 or n < r: return 0
        return self.fact[n] * self.invfact[r] * self.invfact[n-r] % self.mod

    def nPk(self,n,r):
        if n < 0 or n < r: return 0
        return self.fact[n] * self.invfact[n-r] % self.mod


def main():
    N,K=mi()
    graph = [[] for _ in range(N+1)]
    MOD = 10**9+7

    a = 0
    for i in range(N-1):
        a,b=mi()
        graph[a].append(b)
        graph[b].append(a)

    stack = deque([(a,1)])
    seen = set()

    counting = Counting(K+10,MOD)
    ans = counting.nPk(K,1)

    def _len(X):
        cnt = 0
        for x in X:
            if x in seen: continue
            cnt += 1
        # print(X,cnt)
        return cnt

    while len(stack) > 0:
        next,depth = stack.popleft()
        seen.add(next)
        # print("n",next,depth)

        if depth == 1:
            ans *= counting.nPk(K-1,_len(graph[next]))
            ans %= MOD
            # print(_len(graph[next]))
            # print(K-1,len(graph[next]),counting.nPk(K-1,len(graph[next])),"ans",ans)
        # elif depth == 2: continue
        else:
            ans *= counting.nPk(K-2,_len(graph[next]))
            # print(K-1,len(graph[next]),counting.nPk(K-1,len(graph[next])),"ans",ans)
            # print(_len(graph[next]))
            ans %= MOD


        for g in graph[next]:
            if g in seen: continue
            stack.append((g,depth+1))


    print(ans%MOD)



if __name__ == "__main__":
  main()
