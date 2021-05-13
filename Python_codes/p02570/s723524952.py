import sys

def main():
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    a, b, c = data

    if b*c >= a:
        print('Yes')
    else:
        print('No')



if __name__ == '__main__':
    main()
