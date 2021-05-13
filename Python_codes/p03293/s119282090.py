def mi():
    return map(int, input().split())

def ii():
    return int(input())

def main():
    S = input()
    T = input()
    for i in range(len(S)):
        if S == T:
            print('Yes')
            return
        T = T[1:] + T[0]
    print('No')


if __name__ == '__main__':
    main()
