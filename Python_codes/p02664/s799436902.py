import math

def a():
    h1, m1, h2, m2, k = map(int, input().split())
    t1 = h1 * 60 + m1
    t2 = h2 * 60 + m2

    if t1 < t2:
        print(t2 - t1 - k)
    else:
        print(1440 - (t1 - t2) - k)


def b():
    t = input()
    print(t.replace('?','D'))
            



def c():
    print('')



def d():
    print('')


b()