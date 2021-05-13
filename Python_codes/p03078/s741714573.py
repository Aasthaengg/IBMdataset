def resolve():
    X, Y, Z, K = list(map(int, input().split()))
    A = sorted(list(map(int, input().split())), reverse=True)
    B = sorted(list(map(int, input().split())), reverse=True)
    C = sorted(list(map(int, input().split())), reverse=True)
    pushed = set("0-0-0")

    import heapq
    Q = [[-1*(A[0]+B[0]+C[0]), 0, 0, 0]]
    heapq.heapify(Q)
    for i in range(K):
        v, i, j, k = heapq.heappop(Q)
        print(-v)
        if "{}-{}-{}".format(i+1, j, k) not in pushed and i+1 < X:
            heapq.heappush(Q, [-1*(A[i+1]+B[j]+C[k]), i+1, j, k])
            pushed.add("{}-{}-{}".format(i+1, j, k))
        if "{}-{}-{}".format(i, j+1, k) not in pushed and j+1 < Y:
            heapq.heappush(Q, [-1*(A[i]+B[j+1]+C[k]), i, j+1, k])
            pushed.add("{}-{}-{}".format(i, j+1, k))
        if "{}-{}-{}".format(i, j, k+1) not in pushed and k+1 < Z:
            heapq.heappush(Q, [-1*(A[i]+B[j]+C[k+1]), i, j, k+1])
            pushed.add("{}-{}-{}".format(i, j, k+1))

if '__main__' == __name__:
    resolve()