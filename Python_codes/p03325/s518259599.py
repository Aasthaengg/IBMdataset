def mi():
    return map(int, input().split())

def ii():
    return int(input())

def div2(n):
    cnt = 0
    while n%2==0:
        n //= 2
        cnt += 1
    return cnt


def main():
    N = ii()
    a = list(mi())
    print(sum(map(div2, a)))


if __name__ == '__main__':
    main()