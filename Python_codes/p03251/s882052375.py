def mi():
    return map(int, input().split())

def ii():
    return int(input())

def main():
    N, M, X, Y = mi()
    x = list(mi())
    y = list(mi())
    for z in range(-100, 101):
        if max(x) < z <= min(y) and X < z <= Y:
            print('No War')
            return

    print('War')

if __name__ == '__main__':
    main()