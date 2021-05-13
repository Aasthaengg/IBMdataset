from collections import defaultdict
def main():
    d = defaultdict(int)
    n = int(input())
    for _ in range(n):
        d[input()] += 1
    n = int(input())
    for _ in range(n):
        d[input()] -= 1
    print(max(0, *d.values()))

if __name__ == '__main__':
    main()
