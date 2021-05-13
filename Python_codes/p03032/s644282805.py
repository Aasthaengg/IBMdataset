import heapq
def main():
    n, k = map(int, input().split())
    v = list(map(int, input().split()))
    ans = 0
    for L_i in range(min(k+1, n)):#左から取る回数
        R_i_max = k - L_i+1
        if n < L_i + R_i_max:
            R_i_max = n - L_i + 1
        for R_i in range(R_i_max):#右から取る回数
            pop_i = k - L_i - R_i
            q = []
            heapq.heapify(q)
            tmp = 0
            for L_j in range(L_i):
                tmp += v[L_j]
                heapq.heappush(q, v[L_j])
            for R_j in range(n-R_i, n):
                tmp += v[R_j]
                heapq.heappush(q, v[R_j])
            for _ in range(pop_i):
                if len(q) == 0:
                    break
                x = heapq.heappop(q)
                if 0 < x:
                    break
                tmp -= x
            if ans < tmp:
                ans = tmp
    print(ans)

if __name__ == "__main__":
    main()