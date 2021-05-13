def main():
    import sys
    input = sys.stdin.buffer.readline
    N, M = (int(i) for i in input().split())
    cnt = [0]*N
    AB = [[int(i)-1 for i in input().split()] for j in range(M)]
    for a, b in AB:
        cnt[a] += 1
        cnt[b] += 1
    if all(c % 2 == 0 for c in cnt):
        print("YES")
    else:
        print("NO")


if __name__ == '__main__':
    main()
