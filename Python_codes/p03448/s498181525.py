#!/usr/bin/env python3
#
# Author: Tetsuya Ishikawa <tiskw111@gmail.com>
# Date  : June 30, 2020
##################################################### SOURCE START #####################################################

A = int(input().strip())
B = int(input().strip())
C = int(input().strip())
X = int(input().strip())

count = 0

if X % 50 != 0:
    print(0)

else:

    Y = X // 50

    for a in range(A + 1):
        for b in range(B + 1):
            c = Y - 10 * a - 2 * b
            if 0 <= c <= C:
                count += 1

    print(count)

##################################################### SOURCE FINISH ####################################################
# vim: expandtab tabstop=4 shiftwidth=4 fdm=marker
