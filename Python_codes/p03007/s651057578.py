def main():

    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    
    if A[-1] < 0:
        maxv = -sum(A) + 2 * A[-1]
        cur = A[-1]
        ops = []
        for i in range(N-1):
            ops.append([cur, A[i]])
            cur -= A[i]
    elif A[0] >= 0:
        maxv = sum(A)-2*A[0]
        ops = []
        cur = A[0]
        for i in range(1, N-1):
            ops.append([cur, A[i]])
            cur -= A[i]
        ops.append([A[-1], cur])
    else:
        pos = []
        neg = []
        for a in A:
            if a < 0: neg.append(a)
            else: pos.append(a)
        maxv = sum(pos) - sum(neg)
        ops = []
        cur = neg[0]
        for i in range(len(pos)-1):
            ops.append([cur, pos[i]])
            cur -= pos[i]
        ops.append([pos[-1], cur])
        cur = pos[-1] - cur
        for i in range(1, len(neg)):
            ops.append([cur, neg[i]])
            cur -= neg[i]

    return maxv, ops

if __name__ == '__main__':
    output = main()
    print(output[0])
    for a, b in output[1]:
        print(" ".join(map(str, [a, b])))