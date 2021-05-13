#!/usr/bin/env python
# -*- coding: utf-8 -*-

# みんなのプロコン 2019：A - Anti-Adjacency


def main():
    N, K = [int(i) for i in raw_input().strip().split(' ')]

    if N >= K*2 - 1:
        print 'YES'
    else:
        print 'NO'


if __name__ == '__main__':
    main()
