def mi():
    return map(int, input().split())

def ii():
    return int(input())

def main():
    N = ii()
    a = list(mi())
    print(sum(a[i]-1 for i in range(N)))

if __name__ == '__main__':
    main()