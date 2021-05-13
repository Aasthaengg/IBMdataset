def ABC_111_A():
    n = input()
    n = list(n)

    for i in range(len(n)):
        if n[i] == '1':
            n[i] = '9'
        else:
            n[i] = '1'

    n = ''.join(n)
    print(n)

    

if __name__ == '__main__':

    ABC_111_A()