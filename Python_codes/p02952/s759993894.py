#create date: 2020-07-04 09:52

import sys
stdin = sys.stdin

def ns(): return stdin.readline().rstrip()
def ni(): return int(ns())
def na(): return list(map(int, stdin.readline().split()))

def main():
    n = ni()
    keta = len(str(n))
    if keta == 1:
        print(n)
    elif keta == 2:
        print(9)
    elif keta == 3:
        print(9 + (n - 99))
    elif keta == 4:
        print(9 + (999 - 99))
    elif keta == 5:
        print(9 + (999 - 99)  + n - 9999)
    else:
        print(9 + (999 - 99) + (99999 - 9999))

if __name__ == "__main__":
    main()