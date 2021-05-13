import sys
def input(): return sys.stdin.readline().strip()


def main():
    A = list(map(int, input().split()))
    K = int(input())

    def dfs(k):
        if k == 0: return sum(A)
        A[0] *= 2
        cand1 = dfs(k - 1)
        A[0] //= 2
        A[1] *= 2
        cand2 = dfs(k - 1)
        A[1] //= 2
        A[2] *= 2
        cand3 = dfs(k - 1)
        A[2] //= 2
        return max(cand1, cand2, cand3)

    print(dfs(K))

if __name__ == "__main__":
    main()
