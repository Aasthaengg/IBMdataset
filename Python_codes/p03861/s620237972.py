def main():
    
    end, start, divisor = [int(i) for i in input().split()]
    '''
    end = 1
    start = 1000 000 000 000 000 000
    divisor = 3
    '''

    if end % divisor == 0:
        a = start//divisor - end//divisor + 1
    else:
        a = start//divisor - end//divisor

    print(a)

main()