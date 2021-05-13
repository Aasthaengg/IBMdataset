import sys

sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def ii(): return int(input())
def mi(): return map(int, input().split())
def lmi(): return list(map(int, input().split()))
def lmif(n): return [list(map(int, input().split())) for _ in range(n)]
def ss(): return input().split()

def main():
    L, R = mi()

    mod = 2019
    min_mod = mod
    if R - L >= mod:
        print(0)
        return
    
    for i in range(L, R+1):
        for j in range(i+1, R+1):
            if i * j % mod < min_mod:
                min_mod = i * j % mod
        
    print(min_mod)

    return

main()
