import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

def main():
    a = int(input())
    s = input()[:-1]
    if a >= 3200:
        print(s)
    else:
        print('red')

if __name__ == '__main__':
    main()
