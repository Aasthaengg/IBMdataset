import sys
input = sys.stdin.readline

def main():
    N = int(input())
    a_list = list(map(int, input().split()))
    if sum(a_list) % 2 == 1:
        print("NO")
    else:
        print("YES")

if __name__ == '__main__':
    main()