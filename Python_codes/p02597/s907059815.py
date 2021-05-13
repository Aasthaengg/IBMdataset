# ABC174 D
import sys
sys.setrecursionlimit(3*10**5)

N=int(input())
S=input()

def search(l,r):
    # 半開区間
    if l==r:
        return 0
    if S[l]=='R':
        return search(l+1,r)
    if S[r-1]=='W':
        return search(l,r-1)
    return search(l+1,r-1)+1
print(search(0,N))