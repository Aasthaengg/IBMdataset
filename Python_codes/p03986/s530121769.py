def main():
    X = input()
    cs, ct = 0, 0
    for x in X:
        if x == 'T':
            if cs == 0:
                ct += 1
            else:
                cs -= 1
        else:
            cs += 1
    print(ct * 2)
if __name__ == '__main__':
    main()
