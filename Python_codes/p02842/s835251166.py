from math import floor

def main(N, rate=1.08):
    ans = -1
    for x in range(1, N+1):
        if floor(x * 1.08) == N:
            ans = x
    return ans


if __name__ == "__main__":
    N = int(input())
    ans = main(N)
    print(ans if ans > 0 else ':(')
