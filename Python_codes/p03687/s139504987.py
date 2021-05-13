#!/usr/bin python3
# -*- coding: utf-8 -*-

def main():
    S = list(input())
    sr = set(S)
    ret = 100
    for s in sr:
        max_cnt = 0
        cnt = 0
        for t in S:
            if s!=t:
                cnt += 1
            else:
                max_cnt = max(max_cnt, cnt)
                cnt = 0
        max_cnt = max(max_cnt, cnt)
#        print(s,max_cnt)
        ret = min(ret, max_cnt)
    print(ret)

if __name__ == '__main__':
    main()