import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines

def main():
    x,y = map(int, readline().split())

    i = 1
    while x * 2**i <= y:
        i += 1

    ans = i
    print(ans)

if __name__ == "__main__":
    main()
