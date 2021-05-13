from heapq import heapify, heappop, heappush

def main():

    # Aをpriority qにつっこむ
    # 大きい順にM回discountする
    # 最後に総計を計算する

    N, M = map(int,input().split())
    A = list(map(int,input().split()))
    A = [-a for a in A]
    heapify(A)

    while M > 0:
        a = -heappop(A)
        a //= 2
        heappush(A, -a)
        M -= 1
    
    ans = 0
    for a in A:
        ans -= a

    print(ans)

if __name__ == "__main__":
    main()
