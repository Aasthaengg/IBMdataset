def call(n):
    """
    n: int
    output numbers that is multiple of 3 or include '3' (1 <= number <= n)
    
    >>> call(30)
     3 6 9 12 13 15 18 21 23 24 27 30
    """

    line = ''
    for i in range(1, n+1):
        x = i
        if x % 3 == 0:
            line += ' ' + str(i)
            continue
        while x > 0:
            if x % 10 == 3:
                line += ' ' + str(i)
                break
            x //= 10

    print(line)

if __name__ == '__main__':

    i = int(input())
    call(i)