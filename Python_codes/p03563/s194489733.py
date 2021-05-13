
def read_input():
    r = int(input())
    g = int(input())
    return r, g


def submit():
    r, g = read_input()

    print(r + 2*(g - r))



if __name__ == '__main__':
    submit()