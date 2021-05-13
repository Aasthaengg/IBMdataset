import sys

def solve():
    N = int(input())
    playlist = dict()
    time = [0] * (N + 1)
    for i in range(N):
        s, t = map(str, input().split())
        playlist[s] = i
        time[i + 1] = time[i] + int(t)
    w = input()

    print(time[N] - time[playlist[w] + 1])


    return 0

if __name__ == "__main__":
    solve()