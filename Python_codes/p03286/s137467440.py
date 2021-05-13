import sys
from collections import deque
def input(): return sys.stdin.readline().strip()


def main():
    """
    Nを-2べきで展開したときの末端項がmod 2で決定できるから
    末尾から再帰的に桁が決められたのか。。。
    """
    N = int(input())
    if N == 0:
        print(0)
        return
    idx = 0
    ans = deque([])
    while N != 0:
        if N % 2 == 0:
            ans.appendleft(0)
        if N % 2 != 0:
            ans.appendleft(1)
            N -= (-1) ** idx
        N //= 2
        idx += 1
    print("".join(map(str, ans)))    

if __name__ == "__main__":
    main()
