import sys
from itertools import accumulate
def input(): return sys.stdin.readline().strip()


def main():
    N, K = map(int, input().split())
    S = input()

    """
    反転させる区間は独立であるとしてよい。実際反転させる２区間が左図のように
    オーバーラップしていたとすると、これは右図のように反転させるのと同値だからである：
               _______________                             _______  
        ______|_______        |     --->    ______        |       |
    ___|______|_______|_______|_____    ___|______|_______|_______|_____ 
    
    そうすると安直には0がなるべく長く連続している区間に反転をかけたくなるが、
    長い順に反転をかけた場合1が連続する保証がないのでダメ。

    そこで1の連続する箇所を固定したうえで、そこから0の連続する区間に順番に反転をかけることを考える。
    当然愚直にやるとTLEなので、累積和で実装する
    """

    A = []
    char = S[0]
    cnt = 1
    for i in range(1, N):
        if S[i] == char:
            cnt += 1
        else:
            A.append(cnt)
            char = S[i]
            cnt = 1
    A.append(cnt)
    #print("A={}".format(A))

    B = list(accumulate(A))
    B.append(B[-1])
    #print("B={}".format(B))
    l = len(A)
    if S[0] == '0':
        ans = B[min(K * 2 - 1, l - 1)]
        for i in range(1, l - K * 2 + 1):
            if i % 2 == 0:
                j = i + K * 2 - 1
                val = B[j] - B[i - 1]
            else:
                j = i + K * 2
                val = B[j] - B[i - 1]
            #print("[{}, {}]->val={}".format(i, j, val))
            ans = max(ans, val)
    else:
        ans = B[min(K * 2, l - 1)]
        for i in range(1, l - K * 2 + 1):
            if i % 2 == 1:
                j = i + K * 2 - 1
                val = B[j] - B[i - 1]
            else:
                j = i + K * 2
                val = B[j] - B[i - 1]
            #print("[{}, {}]->val={}".format(i, j, val))
            ans = max(ans, val)
    print(ans)
       


if __name__ == "__main__":
    main()
