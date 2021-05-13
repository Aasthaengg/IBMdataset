import sys
input = sys.stdin.buffer.readline
from collections import defaultdict

def main():
    H,W,N = map(int,input().split())
    d = defaultdict(int)
    for i in range(N):
        a,b = map(int,input().split())
        a -= 1
        b -= 1
        for x in range(3):
            for y in range(3):
                na,nb = a-x,b-y
                if (0 <= na < H-2 and 0 <= nb < W-2):
                    d[na*W+nb] += 1
    
    d = list(d.values())
    ans = (H-2)*(W-2)-len(d)
    print(ans)
    for i in range(9):
        i += 1
        print(d.count(i))

if __name__ == "__main__":
    main()