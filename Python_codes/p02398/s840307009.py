if __name__ == '__main__':
    a, b, c = [int(i) for i in input().split()]
    cnt = 0
    for i in range(a, b+1):
        if c%i == 0:
            cnt = cnt+1
    print(cnt)