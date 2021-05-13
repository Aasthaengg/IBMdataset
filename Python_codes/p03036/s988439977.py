import sys
input = sys.stdin.readline
def main():
    r, D, Xtt = map(int, input().split())
    ans = Xtt
    for i in range(10):
        ans = r*ans - D
        print(ans)

if __name__ == '__main__':
    main()