def read_int_list():
    return (int(i) for i in input().split())

n, m = read_int_list()
print((n-1)*(m-1))