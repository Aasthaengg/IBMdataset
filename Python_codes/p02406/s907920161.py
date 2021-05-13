def main():
    n = int(input())
    _list = list(range(1,n+1))
    for x in _list:
        if x % 3 == 0 or any(list(map(lambda x: int(x) == 3, list(str(x))))):
            print(' %d' %  x, end = '')
    print()
    

main()