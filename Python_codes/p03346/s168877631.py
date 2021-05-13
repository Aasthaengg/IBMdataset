def main():
    import sys
    input = sys.stdin.readline
    N = int(input())
    l = [0] * (N + 1)
    for n in range(N):
        p = int(input())
        l[p] = l[p-1] + 1
    print(N - max(l))

if __name__ == '__main__':
    main()