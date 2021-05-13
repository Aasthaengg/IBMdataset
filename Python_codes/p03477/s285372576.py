def main():
    A, B, C, D = map(int, input().split())

    L = A + B
    R = C + D

    if L > R:
        print('Left')
    elif L < R:
        print('Right')
    else:
        print('Balanced')

if __name__ == '__main__':
    main()