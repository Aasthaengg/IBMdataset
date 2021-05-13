#!/usr/bin/env python3
#
# Author: Tetsuya Ishikawa <tiskw111@gmail.com>
# Date  : June 30, 2020
##################################################### SOURCE START #####################################################

N = int(input().strip())
ds = [int(input().strip()) for _ in range(N)]

ds = sorted(ds, reverse=True)
es = [ds.pop(0)]

for d in ds:
    if d < es[-1]: es.append(d)

print(len(es))

##################################################### SOURCE FINISH ####################################################
# vim: expandtab tabstop=4 shiftwidth=4 fdm=marker
