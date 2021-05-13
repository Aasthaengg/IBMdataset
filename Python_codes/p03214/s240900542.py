if __name__ == '__main__':
    n = int(input())
    a = [int(i) for i in input().split()]
    avg = sum(a) / n
    min = 101
    now = 0
    for i in range(n):
        if abs(avg -a[i]) < min:
           min = abs(avg -a[i])
           now = i
    print(now)
