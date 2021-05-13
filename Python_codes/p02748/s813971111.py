def main():
    _,_,m = map(int,input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    res = [0]*(m+1)
    res[-1] = min(a)+min(b)
    for i in range(m):
        x,y,c = map(int,input().split())
        res[i] = a[x-1]+b[y-1]-c
    print(min(res))
if __name__ == '__main__':
    main()
