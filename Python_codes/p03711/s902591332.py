"""AtCoder."""


def get_group(n):
    if n in [1,3,5,7,8,10,12]:
        return 0
    
    if n in [4, 6, 9, 11]:
        return 1

    if n in [2]:
        return 2

def main():
    x, y = map(int, input().split())
    
    if get_group(x) == get_group(y):
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    main()
