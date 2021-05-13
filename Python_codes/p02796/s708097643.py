import sys
input = sys.stdin.buffer.readline
from operator import itemgetter

def main():
    N = int(input())
    arm = []
    for _ in range(N):
        x,l = map(int,input().split())
        arm.append((x-l,x+l))
    
    count = 0
    arm.sort(key=itemgetter(1))
    
    right = -10**10
    for l,r in arm:
        if right <= l:
            right = r
            count += 1
    
    print(count)
    
if __name__ == "__main__":
    main()
