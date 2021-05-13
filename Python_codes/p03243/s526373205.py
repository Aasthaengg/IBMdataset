import bisect

def mi():
    return map(int, input().split())

def ii():
    return int(input())

def main():
    N = int(input())
    l = [111, 222, 333, 444, 555, 666, 777, 888, 999]
    i = bisect.bisect_left(l, N)
    print(l[i])



if __name__ == '__main__':
    main()