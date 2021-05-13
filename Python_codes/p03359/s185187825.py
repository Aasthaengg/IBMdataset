if __name__=='__main__':
    a, b = map(int, input().split())

    day = int(a)-1
    if b >= a:
        day += 1
    print(day)