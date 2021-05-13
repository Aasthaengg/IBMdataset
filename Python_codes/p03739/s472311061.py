import sys
from itertools import accumulate
def input(): return sys.stdin.readline().strip()

def main():
    N = int(input())
    A = list(map(int, input().split()))
    S = list(accumulate(A))

    # 先頭が正の場合
    times_plus = 0
    added = 0
    for i in range(N):
        num = S[i] + added
        if num * (-1)**i > 0: continue
        added += abs(num - (-1)**i) * (-1)**i
        times_plus += abs(num - (-1)**i)
        

    # 先頭が負の場合
    times_minus = 0
    added = 0
    for i in range(1, N + 1):
        num = S[i - 1] + added
        if num * (-1)**i > 0: continue
        added += abs(num - (-1)**i) * (-1)**i
        times_minus += abs(num - (-1)**i)
    
    print(min(times_minus, times_plus))
    

if __name__ == "__main__":
    main()
