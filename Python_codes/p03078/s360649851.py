import sys
from heapq import heappush, heappop
def input(): return sys.stdin.readline().strip()

def main():
    X, Y, Z, K = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    A.sort(reverse=True)
    B.sort(reverse=True)
    C.sort(reverse=True)

    """
    heapqを使う発想は正しかったが、(Ai, *, *)を全てキューに突っ込んで
    Aiを削除しようとしたのが敗因。

    キューの中で(Ai + Bj + Ck)だけではなく(Ai + Bj + Ck, i, j, k)の
    添字まで管理しておけば、最大値を取り出した後にキューに突っ込むのは
        (A(i+1) + Bj + Ck, i+1, j, k)
        (Ai + B(j+1) + Ck, i, j+1, k)
        (Ai + Bj + C(k+1), i, j, k+1)
    の3つだけでよくなる。。。
    """

    q =[(-A[0]-B[0]-C[0], 0, 0, 0)]
    pushed = set([])
    for _ in range(K):
        val, i, j, k = heappop(q)
        print(-val)
        if i < X - 1 and (i+1, j, k) not in pushed:
            heappush(q, (-A[i+1]-B[j]-C[k], i+1, j, k))
            pushed.add((i+1, j, k))
        if j < Y - 1 and (i, j+1, k) not in pushed:
            heappush(q, (-A[i]-B[j+1]-C[k], i, j+1, k))
            pushed.add((i, j+1, k))
        if k < Z - 1 and (i, j, k+1) not in pushed:
            heappush(q, (-A[i]-B[j]-C[k+1], i, j, k+1))
            pushed.add((i, j, k+1))
        #print(q)



if __name__ == "__main__":
    main()
