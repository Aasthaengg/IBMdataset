import sys
from operator import itemgetter

sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def ii(): return int(input())
def mi(): return map(int, input().split())
def lmi(): return list(map(int, input().split()))
def lmif(n): return [list(map(int, input().split())) for _ in range(n)]
def ss(): return input().split()

def main():
    s = input().rstrip()
    len_s = int(len(s))
    children = [0] * len_s
    s += "E"
    start = 0
    now = 0
    while now < len_s-1:
        r = 0
        l = 0
        while s[now] == "R":
            r += 1
            now += 1
        er = now - 1
        sl = now
        while s[now] == "L":
            l += 1
            now += 1
        count = now - start
        if count % 2 == 0:
            children[er] = count // 2
            children[sl] = count // 2
        else:
            if r % 2 == 1:
                children[er] = count // 2 + 1
                children[sl] = count // 2
            else:
                children[er] = count // 2
                children[sl] = count // 2 + 1
        start = now

    print(*children)

    return

main()
