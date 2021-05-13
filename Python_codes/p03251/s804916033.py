def main():
    N,M,X,Y = map(int,input().split())
    x = [int(i) for i in input().split()]
    y = [int(i) for i in input().split()]
    maxx = max(x)
    miny = min(y)
    for z in range(X+1,Y+1):
        if maxx<z and miny>=z:
            print('No War')
            exit()
    print('War')
main()