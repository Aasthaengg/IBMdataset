while 1:
    n = input()
    if n == '0':
        break
    nl = list(map(int,list(n)))
    print(sum(nl))
