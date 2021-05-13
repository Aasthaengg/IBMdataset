import numpy as np
import scipy as sp

def main():
    # parse
    X, A, B = parse(get_stdin())
    # compute
    result = compute(X, A, B)
    # show result
    print(result)

def compute(X, A, B):
    if 0 >= B-A:
        return "delicious"
    elif X >= B-A:
        return "safe"
    else:
        return "dangerous"

def get_stdin():
    return input()

def split_stdin(stdin_val, delimiter = ' '):
    return [x for x in stdin_val.split(delimiter) if x != '']

def parse(stdin_vars):
    vars = split_stdin(stdin_vars)
    return int(vars[0]), int(vars[1]), int(vars[2])

if __name__ == "__main__":
    main()