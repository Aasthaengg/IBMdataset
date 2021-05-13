def main():
    import sys
    input = sys.stdin.readline
    K, T = [int(x) for x in input().strip().split()]
    A = [int(x) for x in input().strip().split()]
    print(max(0, max(A)-(sum(A)-max(A))-1))

if __name__ == '__main__':
     main()