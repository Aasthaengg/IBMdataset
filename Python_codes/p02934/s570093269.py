import sys
read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines

def main():
    N = int(readline())
    A = [int(i) for i in readline().split()]

    ans = 0
    tmp = 0
    for a in A:
        tmp += 1 / a
    
    ans = 1 / tmp
    print(ans)


if __name__ == "__main__":
    main()
