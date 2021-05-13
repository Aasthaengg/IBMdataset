if __name__ == '__main__':
    # n = int(input())
    a, b, x = map(int, input().split())
    c = b//x - a//x
    if a%x == 0:
        c = c+1
    print(c)
