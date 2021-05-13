#!/usr/bin python3
# -*- coding: utf-8 -*-

def cnt(st):
    x = st.copy()
    ret = 0
    for i in range(1,len(st)):
        if x[i]==x[i-1]:
            ret += 1
            x[i] = '0'
    return ret

def main():
    S = list(input())
    K = int(input())
    res1 = cnt(S)
    res2 = cnt(S+S)
    res3 = cnt(S+S+S)
    d1=res2-res1
    d2=res3-res2
    x2=(K-1)//2
    x1=K-1 - x2
    ret=res1+x1*d1+x2*d2
    print(ret)

if __name__ == '__main__':
    main()