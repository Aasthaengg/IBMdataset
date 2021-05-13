def main():
    n = input()

    res = ''

    for i in range(len(n)):
        if n[i] == '1':
            res += '9'
        elif n[i] == '9':
            res += '1'
        else:
            res += n[i]
    
    print(int(res))

if __name__ == '__main__':
    main()