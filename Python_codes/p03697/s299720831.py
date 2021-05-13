

def main():
    a, b = map(int, input().split())
    c = a + b
    if c >= 10:
        print('error')
    else:
        print(c)

if __name__ == '__main__':
    main()
