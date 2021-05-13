import sys
import math
from collections import defaultdict

sys.setrecursionlimit(10**7)
def input():
    return sys.stdin.readline()[:-1]

mod = 10**9 + 7

def I(): return int(input())
def II(): return map(int, input().split())
def III(): return list(map(int, input().split()))
def Line(N):
    read_all = [tuple(map(int, input().split())) for _ in range(N)]
    return map(list,zip(*read_all))

#################

def edges_to_pt(s,t,n,directed=False):
    pt = [[] for _ in range(n)]
    for i in range(len(s)):
        pt[s[i]-1].append(t[i]-1)
        if directed==False:
            pt[t[i]-1].append(s[i]-1)
    return pt

def fact_all(n,M=mod):
    f = [1]*(n)
    ans = 1
    for i in range(1,n):
        ans = ans*i
        ans = ans%M
        f[i] = ans
    return f

def extgcd(a,b):
    r = [1,0,a]
    w = [0,1,b]
    while w[2]!=1:
        q = r[2]//w[2]
        r2 = w
        w2 = [r[0]-q*w[0],r[1]-q*w[1],r[2]-q*w[2]]
        r = r2
        w = w2
    return [w[0],w[1]]

def mod_inv(a,M=mod):
    x = extgcd(a,M)[0]
    return (M+x%M)%M

N,K = II()
if N==1:
    print(K)
    exit()
else:
    a,b = Line(N-1)

pt = edges_to_pt(a,b,N)
v = 0
ans = K
check_visited = [False]*N
check_visited[v] = True
S = [v]
l = 0

f = fact_all(K)
inv = [0]*K
for i in range(K):
    inv[i] = mod_inv(f[i])

while S:
    v1 = S.pop()
    num = 0
    for i in pt[v1]:
        if check_visited[i] == False:
            check_visited[i] = True
            num += 1
            S.append(i)
    if l==0:
        if K-1-num>=0:
            ans *= f[K-1]*inv[K-1-num]
            ans %= mod
            l = 1
        else:
            print(0)
            exit()
    else:
        if K-2-num>=0 and K-2>=0:
            ans *= f[K-2]*inv[K-2-num]
            ans %= mod
        else:
            print(0)
            exit()

print(ans)