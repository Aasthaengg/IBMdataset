import math

url = "https://atcoder.jp//contests/abc057/tasks/abc057_c"

def main():
    x = int(input())
    ans, div = divmod(x, 11)
    ans *= 2
    ans += math.ceil(div/6)
    print(ans)

if __name__ == '__main__':
    main()
