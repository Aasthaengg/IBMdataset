def main():
    N = int(input())
    A = int(input())
    if N <= A:
        print('Yes')
        return
    times = N // 500
    if times*500 + A >= N:
        print('Yes')
    else:
        print('No')
main()