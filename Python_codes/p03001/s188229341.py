def main():
    w, h, x, y = list(map(int, input().split()))
    is_center = 1 if x*2 == w and y*2 == h else 0
    print(f'{w*h / 2.0} {is_center}')

if __name__ == '__main__':
    main()