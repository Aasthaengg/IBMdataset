
url = "https://atcoder.jp//contests/abc061/tasks/abc061_a"

def main():
    t = list(map(int, input().split()))
    print('Yes') if t[0] <= t[2] and t[1] >= t[2] else print('No')

if __name__ == '__main__':
    main()
