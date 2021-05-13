n, k = map(int, input().split())

def main():
    max = (n-1)*(n-2)//2
    if max < k:
        print(-1)
        return 0
    add = max - k
    m = n-1 + add
    print(m)
    for i in range(2,n+1):
        print(1, i)
    for i in range(2, n+1):
        for j in range(i+1, n+1):
            if add <= 0:
                return 0
            print(i, j)
            add -= 1

main()