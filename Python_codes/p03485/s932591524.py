import math

url = "https://atcoder.jp/contests/abc082/tasks/abc082_a"

def main():
    n,m = list(map(int, input().split()))
    print(math.ceil((n + m) / 2))
if __name__ == '__main__':
    main()


