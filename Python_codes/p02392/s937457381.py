def main():

    [str_a, str_b, str_c] = input().split(' ')
    if int(str_a) < int(str_b) and int(str_b) < int(str_c):
        print('Yes')
    else:
        print('No')


main()