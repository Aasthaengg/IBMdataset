import sys
import math
import itertools


# \n
def input():
    return sys.stdin.readline().rstrip()


def main():
    list = [[3, 5, 7]]
    N=int(input())
    for i in range(9):
        new = []
        for j in list[-1]:
            a = 10 * j
            new.append(a + 3)
            new.append(a + 5)
            new.append(a + 7)
        list.append(new)

    pass
    count =0
    for sub in list:
        for j in sub:
            s =str(j)
            if j>N:
                print(count)
                exit()
            if "3" in s and "7" in s and "5" in s:
                count +=1






if __name__ == "__main__":
    main()
