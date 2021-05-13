def main():
    a, b, n = list(map(int, input().split()))
    
    limit = 0
    if n >= b-1:
        limit = b-1
    else:
        limit = n
    
    floor_sub = int(limit * a / b) - int(limit / b) * a
    print(floor_sub)

if __name__ == '__main__':
    main()