import sys
def input(): return sys.stdin.readline().strip()


def main():
    S= input()
    ans = 700
    for i in range(3):
        if S[i] == "o": ans += 100
    print(ans)

if __name__ == "__main__":
    main()
