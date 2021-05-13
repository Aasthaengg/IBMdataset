import sys
input = sys.stdin.buffer.readline
from collections import defaultdict

def main():
    N = int(input())
    pos = [list(map(int,input().split())) for _ in range(N)]
    if N == 1:
        print(1)
    else:
        d = defaultdict(int)
        for i in range(N):
            for j in range(N):
                slope = (pos[i][0]-pos[j][0],pos[i][1]-pos[j][1])
                if slope[0] != 0 or slope[1] != 0:
                    d[slope] += 1
        if len(d) == 0:
            print(N)
        else:
            print(N-max(d.values()))

if __name__ == "__main__":
    main()