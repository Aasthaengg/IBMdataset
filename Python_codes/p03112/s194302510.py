#!/usr/bin/python
# coding: utf-8
import os
from sys import stdin, stdout

if(os.getenv('__LOCAL__')):
    __dirname = os.path.dirname(__file__)
    __basename = os.path.splitext(os.path.basename(__file__))[0]
    __inputname = './input/' + __basename + '.txt'
    __outputname = './output/' + __basename + '.txt'
    __input_path = os.path.join(__dirname, __inputname)
    __output_path = os.path.join(__dirname, __outputname)
    stdin = open(__input_path)
    # stdout = open(__output_path, "w")

def main():
    A, B, Q = map(int, stdin.readline().rstrip().split(' '))
    s = list()
    t = list()
    s.append(-1e12)
    t.append(-1e12)
    s += [int(stdin.readline()) for _ in range(A)]
    t += [int(stdin.readline()) for _ in range(B)]
    X = [int(stdin.readline()) for _ in range(Q)]
    ansvec = list()
    s.append(1e12)
    t.append(1e12)
    # stdout.write("{}\n".format(s))
    # stdout.write("{}\n".format(t))
    # stdout.write("{}\n".format(X))
    for x in X:
        ls = 0
        rs = A+2
        lt = 0
        rt = B+2
        while(rs-ls>1):
            mids=(ls+rs)//2
            if(s[mids]<=x):
                ls = mids
            else:
                rs = mids

        while(rt-lt>1):
            midt=(lt+rt)//2
            if(t[midt]<=x):
                lt = midt
            else:
                rt = midt

        if(t[lt]<=s[ls] and s[rs]<=t[rt]):
            ans = min(abs(t[lt]-x),abs(t[rt]-x))
        elif(s[ls]<=t[lt] and t[rt]<=s[rs]):
            ans = min(abs(s[ls]-x),abs(s[rs]-x))
        elif(s[ls]<=t[lt] and s[rs]<=t[rt]):
            ans = min(abs(s[ls]-x),abs(t[rt]-x), 2*abs(s[rs]-x)+abs(t[lt]-x), 2*abs(t[lt]-x)+abs(s[rs]-x))
        elif(t[lt]<=s[ls] and t[rt]<=s[rs]):
            ans = min(abs(t[lt]-x),abs(s[rs]-x), 2*abs(s[ls]-x)+abs(t[rt]-x), 2*abs(t[rt]-x)+abs(s[ls]-x))
        ansvec.append(ans)

    for a in ansvec:
        stdout.write("{}\n".format(a))

if __name__ == "__main__":
    main()