
def main():
    # parse
    x, y = parse() 
    if y == 1:
        print(0)
    else:
        print(x - y)

def parse():
    vars = split_stdin(get_stdin())
    # var = get_stdin()
    return  int(vars[0]), int(vars[1]) 

def get_stdin():
    return input()

def split_stdin(stdin_val, delim = ' '):
    return [x for x in stdin_val.split(delim) if x != '']

if __name__ == "__main__":
    main()