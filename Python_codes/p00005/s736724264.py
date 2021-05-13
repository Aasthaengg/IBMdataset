# -*-coding:utf-8

import fileinput

def main():
    for line in fileinput.input():
        tokens = list(map(int, line.strip().split()))
        a, b = tokens[0], tokens[1]

        if a < b:
            a, b = b, a

        ansGCD = GreatestCommonDivisor(a, b)
        ansLCM = LeastCommonMultiple(a, b)

        print('{0} {1}'.format(ansGCD, ansLCM))

def GreatestCommonDivisor(a, b):
    while b:
        a, b = b, a%b

    return a

def LeastCommonMultiple(a, b):
    return (a*b) / GreatestCommonDivisor(a, b)


if __name__ == '__main__':
    main()