import sys
from random import randint
from datetime import datetime

sys.setrecursionlimit(10**9)
input = sys.stdin.readline

def ii(): return int(input())
def mi(): return map(int, input().split())
def lmi(): return list(map(int, input().split()))
def lmif(n): return [list(map(int, input().split())) for _ in range(n)]

def randomize(n):
    return [ randint(1, 26) for _ in range(n) ]

def get_now():
    dt = datetime.now()
    return dt.second + dt.microsecond/1000000

def main():
    start = get_now()
    end = get_now()
    # 開催日数
    D = ii()
    # 満足度の下がりやすさ
    C = lmi()
    # 得られる満足度
    S = lmif(D)
    # 開催するコンテスト
    T = randomize(D)

    def scoring():
        # 最後に開かれた日付
        last = [0]*26
        score = 0
        for i in range(D):
            score += S[i][T[i]-1]
            last[T[i]-1] = i+1
            for j in range(26):
                score -= C[j] * (i+1 - last[j])
        return score

    max_score = scoring()
    # print(max_score)
    ans = T.copy()
    # a = 0
    while end - start < 1.95:
        idx, value = randint(0, D-1), randint(1, 26)
        old = T[idx]
        T[idx] = value
        score = scoring()
        if max_score < score:
            ans = T.copy()
            max_score = score
        else:
            T[idx] = old
        # if a % 10000 == 0:
        #     print(a, *T, score, max_score)
        # a += 1
        end = get_now()
    print(*ans, sep='\n')

main()
