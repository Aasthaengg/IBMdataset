def read():
    buf = input()
    return buf


def solve(N):
    count = 0
    for letter in N:
        if letter is '2':
            count += 1

    return count


if __name__ == '__main__':
    inputs = read()
    print(solve(inputs))
