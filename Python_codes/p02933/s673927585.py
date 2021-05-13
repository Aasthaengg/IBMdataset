import sys
input = lambda: sys.stdin.readline().rstrip()
input_nums = lambda: list(map(int, input().split()))

def main():
    a = int(input())
    s = input()
    if a >= 3200:
        print(s)
    else:
        print('red')
if __name__ == '__main__':
    main()