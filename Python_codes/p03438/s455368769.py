import sys
sys.setrecursionlimit(10 ** 9 + 10)
def input(): return sys.stdin.readline().strip()


def resolve():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    biggerA = 0
    biggerB = 0
    task = 0
    for i in range(N):
        # A[i]>B[i]なる全てのB[i]を埋めてA[i]<=B[i]とできれば勝ち
        if A[i] > B[i]:  # B[i]をcnt分埋めるというタスクがある
            task += A[i] - B[i]
        if A[i] < B[i]:  # B[i]が優っている箇所でA[i]を埋めてタスクを解消
            task -= (B[i] - A[i]) // 2

    if task <= 0:
        print('Yes')
    else:
        print('No')


resolve()