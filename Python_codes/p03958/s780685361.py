import heapq
def main():
    k,t=map(int,input().split())
    a=list(map(lambda x: (-int(x[1]), x[0]+1), enumerate(input().split())))
    heapq.heapify(a)
    p=None
    while len(a) > 0:
        n=heapq.heappop(a)
        if len(a) == 0:
            print(-n[0]-1)
            break
        if p == n[1] and len(a) > 0:
            n2 = n
            n = heapq.heappop(a)
            heapq.heappush(a, n2)
        if n[0] < -1:
            heapq.heappush(a, (n[0]+1, n[1]))
        p = n[1]
    
if __name__ == "__main__":
    main()