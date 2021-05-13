import sys
input = lambda: sys.stdin.readline().rstrip()

def main():
    n, l = map(int, input().split())
    apple = [l+i-1 for i in range(1, n+1)]
    if apple[-1] < 0:
        print(sum(apple[:-1]))
    elif apple[0] > 0:
        print(sum(apple[1:]))
    else:
        print(sum(apple[:]))
    
if __name__ == '__main__':
    main()