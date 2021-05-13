if __name__ == '__main__':
    n,a,b = map(int, input().split())
    minN = a+ b+ (n-2)*a
    maxN = a+ b+ (n-2)*b
    calc = max(maxN-minN+1,0)
    print(calc)
