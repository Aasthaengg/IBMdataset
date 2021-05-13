#!/usr/bin/env python3
#
# Author: Tetsuya Ishikawa <tiskw111@gmail.com>
# Date  : June 30, 2020
##################################################### SOURCE START #####################################################

a, b = tuple(map(int, input().strip().split()))

if a % 2 == 0 or b % 2 == 0:
    print("Even")
else:
    print("Odd")

##################################################### SOURCE FINISH ####################################################
# vim: expandtab tabstop=4 shiftwidth=4 fdm=marker
