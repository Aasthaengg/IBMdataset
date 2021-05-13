#!/usr/bin/env python3
#
# Author: Tetsuya Ishikawa <tiskw111@gmail.com>
# Date  : June 30, 2020
##################################################### SOURCE START #####################################################

cs = ["dream", "dreamer", "erase", "eraser"]
S = input().strip()

while True:

    changed = False

    for c in cs:
        if S.endswith(c):
            S = S[:-len(c)]
            changed = True
            break
    
    if len(S) == 0:
        print("YES")
        break

    if not changed:
        print("NO")
        break

##################################################### SOURCE FINISH ####################################################
# vim: expandtab tabstop=4 shiftwidth=4 fdm=marker
