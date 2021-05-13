def main():
    s = input()

    res = 0

    for sign in s:
        if sign == '+':
            res += 1
        else:
            res -= 1
    
    print(res)

if __name__ == '__main__':
    main()