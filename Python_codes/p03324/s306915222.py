from itertools import permutations

def mi():
    return map(int, input().split())

def ii():
    return int(input())

def main():
    D, N = mi()
    if N == 100:
        print(100**D*101)
    else:
        print(100**D*N)

if __name__ == '__main__':
    main()