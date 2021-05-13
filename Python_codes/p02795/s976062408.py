#-*-coding:utf-8-*-

import math

def main():
    h = int(input())
    w = int(input())
    n = int(input())
    if w >= h:
        ans = math.ceil(n/w)
    else:
        ans = math.ceil(n/h)
    print(ans)

if __name__=="__main__":
    main()