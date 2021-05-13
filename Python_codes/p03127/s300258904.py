def main():
    n = int(input())
    a = list(map(int, input().split()))
    m = min(a)
    next_m = m
    count = 0
    while count != n:
        m = next_m
        count = 0
        pre = a[0]
        for i in range(n):
            if a[i] == pre:
                count += 1
            a[i] %= m
            if a[i] != 0:
                next_m = min(next_m, a[i])
            else:
                a[i] = m
            pre = a[i]
    print(m)
    
if __name__ == '__main__':
    main()