#
# author Sidratul
#

from math import prod

if __name__ == '__main__':
    n = input()
    a = list(map(int, input().split(' ')))
    s = 1
    a.sort()
    x = True
    for i in range(len(a)):
        s = s * a[i]
        if s > 10**18:
            print(-1)
            x = False
            break
    if x:
        print(s)