def main():
    x, y = map(int, input().split())
    flag = False
    if 2 * x <= y <= 4 * x:
        if (4 * x - y) % 2 == 0:
            if (y - 2 * x) % 2 == 0:
                flag = True
                
    if flag:
        print('Yes')
    else:
        print('No')
            

if __name__ == '__main__':
    main()