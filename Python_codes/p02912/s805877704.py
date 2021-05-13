def main():
    import heapq
    n,m = map(int,input().split())
    a = list(map(int,input().split()))
    A = []
    for i in range(n):
        heapq.heappush(A,-1*a[i])
    for i in range(m):
        a = heapq.heappop(A)
        a = (-1*a)//2
        heapq.heappush(A,-1*a)
    print(-1*sum(A))

if __name__ == "__main__":
    main()
