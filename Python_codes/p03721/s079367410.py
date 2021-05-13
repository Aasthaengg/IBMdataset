import sys
def input(): return sys.stdin.readline().strip()
offset = 10**6

def main():
    N, K = map(int, input().split())
    pair = []
    for _ in range(N):
        a, b = map(int, input().split())
        pair.append((a * offset + b))
    pair.sort()
    num = 0
    for val in pair:
        a, b = val // offset, val % offset
        if num + b < K:
            num += b
            continue
        print(a)
        return


    for p in path: print(p)


if __name__ == "__main__":
    main()
