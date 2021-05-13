import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    n = int(input())
    v = sorted(list(map(int, input().split())))
    for _ in range(n-1):
        v.append((v.pop(0) + v.pop(0)) / 2)
        v.sort()
    print(*v)

if __name__ == '__main__':
    main()