def main():
    line = input()
    A, B = [int(n) for n in line.split()]
    if A <= 8 and B <= 8 and A + B <= 16:
        print('Yay!')
    else:
        print(':(')
main()
