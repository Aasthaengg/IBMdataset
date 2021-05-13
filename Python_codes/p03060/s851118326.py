def main():
    g = 0
    n = int(input())
    v = list(map(int,input().split()))
    c = list(map(int,input().split()))
    for i in range(n):
        gain = v[i] -c[i]
        if gain > 0 :
            g += gain
    print(g)


if __name__ == '__main__':
    main()