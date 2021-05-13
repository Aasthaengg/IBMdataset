

def read_input():
    n, m = map(int, input().split())

    return n, m

def submit():
    n, m = read_input()
    print((n - 1)*(m - 1))



if __name__ == '__main__':
    submit()