if __name__ == '__main__':
    n = list(input())
    if n[-1] in ['2', '4', '5', '7', '9']:
        print('hon')
    elif n[-1] in ['3']:
        print('bon')
    else:
        print('pon')