#Haiku
def ABC_51_A():
    s = input()
    s = list(s)
    s[5] = ' '
    s[13] = ' '
    s = ''.join(s)
    print(s)


if __name__ == '__main__':

    ABC_51_A()