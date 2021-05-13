import collections

def main():
    N = int(input())
    A = list(map(int, input().split()))
    c = collections.Counter(A)
    ans = 0
    for num, freq in c.items():
        if num < freq:
            ans += freq - num
        elif num > freq:
            ans += freq
    print(ans)


if __name__ == '__main__':
    main()
