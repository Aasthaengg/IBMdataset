(lambda *_: None)(
    *map(print,
         map('{0[0]} {0[1]}'.format,
             map(lambda ss: sorted(ss, key=int),
                 map(str.split,
                     iter(input, '0 0'))))))