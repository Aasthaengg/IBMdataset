import sys
input = sys.stdin.buffer.readline
import heapq

def main():
    N,Q = map(int,input().split())
    event = []
    
    for _ in range(N):
        s,t,x = map(int,input().split())
        event.append((s-x,1,x))
        event.append((t-x,0,x))
        
    for i in range(Q):
        a = int(input())
        event.append((a,2,i))
    
    event.sort()
    ans = [-1]*Q
    use = set()
    stop = []
    
    for a,b,c in event:
        if b == 1:
            use.add(c)
            heapq.heappush(stop,c)
        elif b == 0:
            use.remove(c)
        else:
            while stop and stop[0] not in use:
                heapq.heappop(stop)
            ans[c] = -1 if len(stop) == 0 else stop[0]
    
    for num in ans:
        print(num)

if __name__ == "__main__":
    main()
