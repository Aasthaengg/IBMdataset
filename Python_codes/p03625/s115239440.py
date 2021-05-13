import sys
from collections import defaultdict
def input(): return sys.stdin.readline().strip()

def main():
    N = int(input())
    A = list(map(int, input().split()))
    d = defaultdict(int)
    for a in A: d[a] += 1
    cand = []
    for key in d:
        for _ in range(d[key] // 2): cand.append(key)
    cand.sort(reverse=True)
    if len(cand) < 2:
        print(0)
        return
    print(cand[0] * cand[1])
    
    


if __name__ == "__main__":
    main()
