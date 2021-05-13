import sys
def input():return sys.stdin.readline().strip()
from collections import Counter

def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for _ in range(M):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)

    ca = Counter(A)
    cb = Counter(B)
    c = ca + cb
    
    if all(count%2 == 0 for count in c.values()):
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()