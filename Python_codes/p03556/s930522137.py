if __name__ == '__main__':
    n =int(input())
    max = 1
    for i in range(1,n):
        now = i*i
        if now > n:
            break
        max = now
    print(max)