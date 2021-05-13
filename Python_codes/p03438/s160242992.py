def main():
    import sys
    import time
    input = sys.stdin.readline
    N = int(input())
    A = [int(x) for x in input().strip().split()]
    B = [int(x) for x in input().strip().split()]
    cnt = 0
    for a, b in zip(A, B):
        a_b = a - b
        if a_b > 0:
            cnt += a_b
        elif a_b < 0:
            cnt -= -a_b // 2
    
    if cnt <= 0:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()