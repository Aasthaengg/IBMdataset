#!/usr/bin/env python3

if __name__ == '__main__':

    a = input().split(' ')
    b = []
    for i in a:
        if i == '+':
            tmp = b.pop(-1) + b.pop(-1)
            b.append(tmp)
        elif i == '-':
            p = b.pop(-1)
            tmp = b.pop(-1) - p
            b.append(tmp)
        elif i == '*':
            tmp = b.pop(-1) * b.pop(-1)
            b.append(tmp)
        else:
            b.append( int(i) )
    print(b[0])