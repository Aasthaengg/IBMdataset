import sys
from collections import defaultdict
def input(): return sys.stdin.readline().strip()

def main():
    N = int(input())
    A = list(map(int, input().split()))
    rate = set()
    top = 0
    for a in A:
        if a >= 3200:
            top += 1
        else:
            rate.add(a // 400)
    print("{} {}".format(max(1, len(rate)), len(rate) + top))
    
    

if __name__ == "__main__":
    main()
