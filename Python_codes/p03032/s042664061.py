import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines
from heapq import heapify, heappop, heappush 
def main():
    N, K = map(int, readline().split())
    V = [int(i) for i in readline().split()]
    A = V[::-1]
    ans = 0
    for l in range(K+1):
        for r in range(K+1-l):
            if l+r>N:
                continue
            rest = K-(l+r)
            hp = V[:l] + A[:r]
            heapify(hp)
            for _ in range(rest):
                if len(hp)==0:
                    break
                v = heappop(hp)
                if v > 0:
                    heappush(hp, v)
            ans = max(ans, sum(hp))
    print(ans)
if __name__ == '__main__':
    main()
