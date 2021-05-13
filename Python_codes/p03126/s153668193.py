import sys

input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    cnt = set(range(1, M+1))
    for _ in range(N):
        K, *A = map(int, input().split())
        cnt.intersection_update(set(A))
    ans = len(cnt)
    print(ans)

if __name__ == "__main__":
    main()
