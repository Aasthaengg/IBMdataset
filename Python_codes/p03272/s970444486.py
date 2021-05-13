def main():
    # parse
    N, i = parse()
    # compute
    result = compute(N, i)
    # show result
    print(result)

def compute(N, i):
    return N + 1 - i

def parse():
    vars = split_stdin(get_stdin())
    return int(vars[0]), int(vars[1])

def get_stdin():
    return input()

def split_stdin(stdin_val, delim = ' '):
    return [x for x in stdin_val.split(delim) if x != '']

if __name__ == "__main__":
    main()