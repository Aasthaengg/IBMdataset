import sys

input = sys.stdin.read

def main(H, N, tmp):
    damage = tmp[::2]
    magic = tmp[1::2]
    DP = [float('inf')] * 20001
    DP[0] = 0
    for i in range(20001):
        for j in range(N):
            s = i - damage[j]
            if s >= 0:
                DP[i] = min(DP[i], DP[s] + magic[j])
    return min(DP[H:])


if __name__ == "__main__":
    H, N, *tmp = map(int, input().split())
    ans = main(H, N, tmp)
    print(ans)
