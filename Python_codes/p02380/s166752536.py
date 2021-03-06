import math


def main():
    """
       /|
    b / | h
     /  |
    /??????|???_
    <- a -->

    ??????a, ??????b, a??¨b??????????§?C(???)
    C???????????????radian????±???????

    ??????1????????????: x
    ??????: h (b?????????????????¨????????????sin????????¨???????±???????
    ??¢???: S (??????)

    L (x + a + b): ??????????????????????????¨??????
    x = sqrt(a_ ** 2 + h ** 2)
    ??????a??????????????????h?????§???????????? a_ ??¨????????¨
    a_ = a - b * cos(rad)
    ??? ??????????????¨?????????????????? ??§??°??°??£??????????????????
    """
    a, b, C = map(int, input().split())

    # ????§???¢????????? 0 < C < 180
    rad = math.pi * C / 180
    sin = math.sin(rad)
    h = b * sin
    S = a * h / 2

    a_ = a - b * math.cos(rad)
    len_d = math.sqrt(a_ ** 2 + h ** 2)

    print("{:.8f}".format(S))
    print("{:.8f}".format(a + b + len_d))
    print("{:.8f}".format(h))

if __name__ == "__main__":
    main()