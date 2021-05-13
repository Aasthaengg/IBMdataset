import sys
def input(): return sys.stdin.readline().strip()

def main():
    N = int(input())
    money = 0
    for _ in range(N):
        x, u = input().split()
        if u == "JPY": money += int(x)
        else: money += float(x) * 380000
    print(money)


if __name__ == "__main__":
    main()
