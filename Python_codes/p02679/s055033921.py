import sys, bisect, collections, math
input = lambda: sys.stdin.readline().rstrip() 
sys.setrecursionlimit(10**7)
INF = 10**20
MOD = 1000000007
def I(): return int(input())
def F(): return float(input())
def S(): return input()
def LI(): return [int(x) for x in input().split()]
def LI_(): return [int(x)-1 for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LS(): return input().split()

def resolve():
    N = I()
    AB = [LI() for _ in range(N)]

    # A, Bを標準化 互いに疎でAは正
    def normalize(AB):
        A = AB[0]
        B = AB[1]
        if A==B==0:
            return (0, 0)
        elif A==0:
            return(0, 1)
        elif B==0:
            return(1, 0)
        else:
            gcd = math.gcd(A, B)
            A //= gcd
            B //= gcd
            if A<0:
                A, B = -A, -B
            return (A, B)
    
    def orthogonal(AB):
        A = AB[0]
        B = AB[1]
        if B>0:
            return (B, -A)
        else:
            return(-B, A)

    AB_n = [normalize(i) for i in AB]
    counter = collections.Counter(AB_n)

    # 場合の数を求める
    used = set()
    ans = 1
    # (0, 0)以外について
    for A, B in AB_n:
        if not (A, B) in used:
            if (A, B)!=(0, 0):
                ans *= pow(2, counter[(A, B)], MOD) + pow(2, counter[orthogonal((A, B))], MOD) - 1
                ans %= MOD
                used.add((A, B))
                used.add(orthogonal((A, B)))
    ans -= 1
    # (0, 0)について
    ans += counter[(0, 0)]
    ans %= MOD

    print(ans)

if __name__ == '__main__':
    resolve()
