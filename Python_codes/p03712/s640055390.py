"""AtCoder."""


def main():
    h, w = map(int, input().split())
    print('#' * (w + 2))
    for _ in range(h):
        print('#' + input() + '#')
    print('#' * (w + 2))

if __name__ == '__main__':
    main()
