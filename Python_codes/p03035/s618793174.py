import sys
input = lambda: sys.stdin.readline().rstrip()
input_nums = lambda: list(map(int, input().split()))

def main():
    A, B = input_nums()
    if A >= 13:
        fee = B
    elif A >= 6:
        fee = B//2
    else:
        fee = 0
    print(fee)

if __name__ == '__main__':
    main()
