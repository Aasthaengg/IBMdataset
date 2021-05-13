def main():
    N = int( input())
    for x in range(1,3501):
        for y in range(1, 3501):
            if 4*x*y <= N*(x+y):
                continue
            if N*x*y%(4*x*y-N*(x+y)) == 0:
                print(x, y, N*x*y//(4*x*y-N*(x+y)))
                return
if __name__ == '__main__':
    main()
