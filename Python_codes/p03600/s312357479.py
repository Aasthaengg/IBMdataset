
import sys
sys.setrecursionlimit(10 ** 7)
read = sys.stdin.buffer.read
inp = sys.stdin.buffer.readline
def inpS(): return inp().rstrip().decode()
readlines = sys.stdin.buffer.readlines
MOD = 10**9+7
INF = 1<<60
# A：想定する最短距離と計算(WF)で算出した最短距離が合っているか判定
# A[i][j] > A[i][k] + A[k][j] : -1
# AとWFが合っていたら最短距離の和を出力
def resolve():
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    B = [[True]*(N) for _ in range(N)]

    for k in range(N):
        for i in range(N):
            for j in range(N):
                if A[i][j] > A[i][k] + A[k][j]:
                    print(-1)
                    return
                # 1~Nまでの最短距離を求める為、不要な道を削除
                # (sample1:1->3=3, 1->2->3=1+2) よって1->3は削除
                elif A[i][j] == A[i][k] + A[k][j] and k!=i and k!= j:
                    B[i][j] = False

    ans = [sum([A[i][j] for j in range(N) if B[i][j]]) for i in range(N)]
    print(sum(ans)//2)

if __name__ == "__main__":
    resolve()