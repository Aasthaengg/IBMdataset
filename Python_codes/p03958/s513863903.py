import heapq

def main():
    K, T = map(int, input().split())
    a = list(map(int, input().split()))
    if T == 1:
        print(K-1)
        return
    b = [-x for x in a]
    heapq.heapify(b)
    tmp = heapq.heappop(b)
    for i in range(K):
        tmp2 = heapq.heappop(b)
        if tmp2 == 0:
            break
        heapq.heappush(b, tmp+1)
        tmp = tmp2
    print(K-1-i)
    
if __name__ == "__main__":
    main()
