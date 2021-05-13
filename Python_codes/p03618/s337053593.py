
import sys
from collections import deque
import copy
import math

class manacher:
    """Cache radius array of palindrome to judge in linear time."""

    def __init__(self, l):
        """Insert '&' to judge both even and odd length palindrome."""
        self.n = len(l)
        self.m = 2*self.n+1
        self.d = ['&']*self.m
        self.r = [0]*self.m
        for i in range(self.n):
            self.d[2*i+1] = l[i]
        self.make_r()

    def make_r(self):
        """Make self.r[i] (radius of palindrome whose center is self.d[i])."""
        i, j = 0, 0
        while i < self.m:
            while j <= i < self.m-j and self.d[i-j] == self.d[i+j]:
                j += 1
            self.r[i] = j
            k = 1
            while k <= i < self.m-k and k+self.r[i-k] < j:
                self.r[i+k] = self.r[i-k]
                k += 1
            i += k
            j -= k

    def judge(self, start, end):
        """Return 1 if l[start, end) is a palindrome."""
        center = start+end
        return 2*end-1 < center+self.r[center]

    def get_num(self, center):
        return self.r[center]


def get_read_func(fileobject):
    if fileobject == None :
        return raw_input
    else:
        return fileobject.readline


def main():
    if len(sys.argv) > 1:
        f = open(sys.argv[1])
    else:
        f = None
    read_func = get_read_func(f);
    input_raw = read_func().strip().split()
    [S] = [(input_raw[0])]
    dic = {}
    for s in S:
        if s not in dic:
            dic[s] = 1
        else:
            dic[s] += 1
    count = len(S) * (len(S) - 1)/2 + 1
    for s in dic:
        count -= dic[s] * (dic[s] - 1)/2
    print count

##    mana = manacher(S)
##    s = 0
##    for i in range(0, len(S) * 2, 2):
##        #print (mana.get_num(i) + mana.get_num(i + 1)) /2,
##        s += (mana.get_num(i) + mana.get_num(i + 1)) /2

    #print (len(S) * (len(S) + 1))/2 - s + 1


if __name__ == '__main__':
    main()
