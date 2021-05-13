import sys

sys.setrecursionlimit(100000)
class Cmber:
    def __init__(self,gensize,mod=10**9+7):
        self.mod = mod
        self.g1=[1,1]
        self.g2 = [1, 1] #逆元テーブル
        self.inverse = [0, 1] #逆元テーブル計算用テーブル
        self.getgen(gensize)
    def getgen(self,N):
        for i in range( 2, N + 1 ):
            self.g1.append( ( self.g1[-1] * i ) % self.mod )
            self.inverse.append( ( -self.inverse[self.mod % i] * (self.mod//i) ) % self.mod )
            self.g2.append( (self.g2[-1] * self.inverse[-1]) % self.mod )
    def per(self,n,r):
        if ( r<0 or r>n ):
            return 0

        return self.g1[n] * self.g2[n-r]  % self.mod        


    def cmb(self,n, r):
        if ( r<0 or r>n ):
            return 0
        r = min(r, n-r)
        return self.g1[n] * self.g2[r] * self.g2[n-r] % self.mod
 
    def cmb_very_high_n(self,n, r):
        if ( r<0 or r>n ):
            return 0
        g1=1
        r = min(r, n-r)
        for i in range(n-r+1,n+1):
            g1*=i
            g1%=self.mod
        return g1 * self.g2[r] % self.mod

    def multiple_cmb(self,vals):
        ans = self.g1[sum(vals)] % self.mod
        for i in vals:
            ans = (ans*self.g2[i])%self.mod
        return ans






def dfs(connections:list,node,oya,K,cmber:Cmber):

    if node == oya:
        children = connections[node]
        ans = cmber.per(K-1,len(children))

        for child in children:
            ans *= dfs(connections,child,node,K,cmber)
            ans %= cmber.mod

        return (ans * K) % cmber.mod

    if len(connections[node])==1:

        return 1


    children = [i for i in connections[node] if i != oya]

    ans = cmber.per(K-2,len(children))
    for child in children:
        ans *= dfs(connections,child,node,K,cmber)
        ans %= cmber.mod

    return ans





def resolve():
    N,K = map(int,input().split())
    connections= [[] for i in range(N)]
    for i in range(N-1):
        a,b = map(int,input().split())
        connections[a-1].append(b-1)
        connections[b-1].append(a-1)

    cmber = Cmber(K)
    print(dfs(connections,0,0,K,cmber))







if __name__ == "__main__":
    resolve()