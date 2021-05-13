def ALDS1_4C():
    D = {}
    for i in range(int(input())):
        cmd, key = input().split()
        if cmd == 'insert':
            D[key]='yes'
        else:
            print(D.get(key, 'no'))

if __name__ == '__main__':
    ALDS1_4C()