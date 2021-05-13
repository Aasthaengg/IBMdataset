import sys
input = sys.stdin.readline

def main():
    H,W,D = map(int,input().split())
    A = [None] * (H*W+1)
    for i in range(H):
        j = 1
        for x in input().split():
            # [消費魔力の総和, 座標]
            A[int(x)] = [0,(i+1,j)]
            j += 1

    # 累積和を求める O(H*W)
    for i in range(1,H*W+1):
        if i <= D:
            continue
        A[i][0] += A[i-D][0]
        A[i][0] += abs(A[i][1][0] - A[i-D][1][0])
        A[i][0] += abs(A[i][1][1] - A[i-D][1][1])

    # クエリ O(1)
    Q = int(input())
    for _ in range(Q):
        L, R = map(int,input().split())

        print(A[R][0] - A[L][0])

if __name__ == "__main__":
    main()