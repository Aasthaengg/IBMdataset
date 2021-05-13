def main():
    from collections import deque

    N = int(input())
    A = input().split()

    ret = deque()
    head_is_0 = 1
    for x in A:
        if head_is_0:
            ret.append(x)
        else:
            ret.appendleft(x)
        head_is_0 ^= 1

    if head_is_0 == 0:
        ret.reverse()
    print(*ret)


if __name__ == '__main__':
    main()
