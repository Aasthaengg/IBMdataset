
def read_input():
    a, b, c = map(int, input().split())
    return a, b, c

def submit():
    a, b, c = read_input()

    if a <= c <= b:
        print('Yes')
    else:
        print('No')


if __name__ == '__main__':
    submit()