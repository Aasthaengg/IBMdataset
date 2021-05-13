# -*- coding: utf-8 -*-

def main():

    A, op , B = map(str, input().split())

    if op == '+':
        ans = int(A) + int(B)
    
    elif op == '-':
        ans = int(A) - int(B)

    print(ans)


if __name__ == "__main__":
    main()