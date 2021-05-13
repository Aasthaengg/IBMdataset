from sys import stdin
readline = stdin.readline
def i_input(): return int(readline().rstrip())
def i_map(): return map(int, readline().rstrip().split())
def i_list(): return list(i_map())


def main():
    N = i_input()
    ans = 0
    for a in range(1, N):
        ans += (N - 1) // a
    print(ans)

if __name__ == "__main__":
    main()
