#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import scipy as sp

def main():
    try:
        input_list = input().split()
        N = int(input_list[0])
        K = int(input_list[1])
        print(N-K+1);
    except:
        pass

if __name__ == '__main__':
    main()
