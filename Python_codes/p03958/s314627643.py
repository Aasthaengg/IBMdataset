from sys import stdin

def main():
    input = stdin.readline
    k, _ = map(int, input().split())
    a = max(map(int, input().split()))
    print(max(0, 2 * a - k - 1))
main()