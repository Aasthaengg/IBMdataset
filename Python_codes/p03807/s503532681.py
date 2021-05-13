import sys
input = sys.stdin.readline

def main():
    N = int(input())
    a_list = list(map(int, input().split()))
    odds = [a for a in a_list if a % 2 == 1]
    if len(odds) % 2 == 1:
        print("NO")
    else:
        print("YES")

if __name__ == '__main__':
    main()
