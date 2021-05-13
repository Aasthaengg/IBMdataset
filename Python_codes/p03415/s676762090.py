import sys
def input(): return sys.stdin.readline().strip()


def main():
    C = [input() for _ in range(3)]
    ans = C[0][0] + C[1][1] + C[2][2]
    print(ans)

if __name__ == "__main__":
    main()
