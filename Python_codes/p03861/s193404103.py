def input_int():
    return(int(input()))

def input_int_list():
    return(list(map(int,input().split())))

def input_int_map():
    return(map(int,input().split()))


def run():
    a, b, x = input_int_map()
    result = count_num(b, x) - count_num(a - 1, x)
    print(result)

def count_num(num, x):

    if num < 0:
        return 0

    return num // x + 1

run()

# 2 4 3

# 3 4 3

# 2 6 3















