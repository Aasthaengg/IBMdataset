import sys
input = lambda: sys.stdin.readline().rstrip()

def main():

    from heapq import heappop, heappush, heapify
    X,Y,Z,K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))

    A.sort(reverse=True)
    B.sort(reverse=True)
    C.sort(reverse=True)

    sum_list = []
    seen_list = set()
    ans = []

    heappush(sum_list, (-(A[0]+B[0]+C[0]), 0, 0, 0))
    seen_list.add((0, 0, 0))

    for _ in range(K):
        s, i, j, k = heappop(sum_list)
        
        ans.append(-s)

        if i+1 < len(A) and (i+1, j, k) not in seen_list:
            heappush(sum_list, (-(A[i+1]+B[j]+C[k]), i+1, j, k))
            seen_list.add((i+1, j, k))

        if j+1 < len(B) and (i, j+1, k) not in seen_list:
            heappush(sum_list, (-(A[i]+B[j+1]+C[k]), i, j+1, k))
            seen_list.add((i, j+1, k))

        if k+1 < len(C) and (i, j, k+1) not in seen_list:
            heappush(sum_list, (-(A[i]+B[j]+C[k+1]), i, j, k+1))
            seen_list.add((i, j, k+1))

    for i in range(0, K):
        print(ans[i])

if __name__ == "__main__":
    main()