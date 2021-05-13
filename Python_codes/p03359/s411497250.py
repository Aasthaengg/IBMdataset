def main():
    a,b = list(map(int,input().split()))
    print(solve(a,b))
def solve(a,b):
    m = a-1
    n = 1 if a <= b else 0
    return m + n

if __name__ == '__main__':
    main()
