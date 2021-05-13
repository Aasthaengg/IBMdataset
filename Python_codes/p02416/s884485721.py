import functools


def sum_of_digits(digits):
    """culculate the sum of each digit of 'digits'

    >>> sum_of_digits("123")
    6
    >>> sum_of_digits("100")
    1
    >>> sum_of_digits("")
    0
    """
    return functools.reduce(lambda x, y: x+int(y), digits, 0)


def run():
    d = input()

    while d != '0':
        print(sum_of_digits(d))
        d = input()


if __name__ == '__main__':
    run()

