import sys
from itertools import accumulate
def input(): return sys.stdin.readline().strip()


def main():
    N, K = map(int, input().split())
    S = input()

    """
    chokudaiさんのコードも尺取りで写経してみる！
    """

    A = []
    char = 1 # 必ず１から始まるようにするのかなるほど。。。
    cnt = 0
    for i in range(N):
        if S[i] == str(char):
            cnt += 1
        else:
            A.append(cnt)
            char = 1 - char
            cnt = 1
    if cnt != 0: A.append(cnt)
    if len(A) % 2 == 0: A.append(0)
    #print(A)

    """
    この時点でA = [(1の個数), (0の個数), (1の個数), (0の個数),...,(1の個数)]
    のように並んでいるので、Sの先頭が0か1かの場合分けが不要になるし、
    以降の尺取りは(1の個数)のところから常にカウントを始めて良い。
    """

    add = K * 2 + 1
    ans = 0
    left = 0
    right = 0
    tmp = 0 # [left, right)の値

    i = 0
    l = len(A)
    while i < l:
        nextLeft = i
        nextRight = min(i + add, l)
        while nextLeft > left:
            tmp -= A[left]
            left += 1
        while nextRight > right:
            tmp += A[right]
            right += 1
        ans = max(ans, tmp)
        i += 2
    print(ans)


if __name__ == "__main__":
    main()
