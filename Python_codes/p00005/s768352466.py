import sys

def main():
    """ ????????? """
    MAX = 2000000000
    istr = sys.stdin.read()
    wi = istr.splitlines()
    for i in wi:
        a, b = list(map(int,i.split()))
        if a < b:
            a, b = b, a

        """ ????????????????????????????????§?????§??¬?´???°????????? """
        x = a
        y = b
        while y > 0:
            z = x % y
            x = y
            y = z

        """ a ??¨ b ????????? a ??¨ b ???????°???¬?´???°??§?????? """
        l = a * b // x

        print("{} {}".format(x,l))

if __name__ == '__main__':
    main()