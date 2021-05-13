def mi():
    return map(int, input().split())

def ii():
    return int(input())

def main():
    N = ii()
    S = set(input().split())
    if len(S) == 3:
        print('Three')
    else:
        print('Four')


if __name__ == '__main__':
    main()