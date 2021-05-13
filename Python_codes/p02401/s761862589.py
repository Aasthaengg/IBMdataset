from itertools import takewhile
(lambda *_: None)(*map(print,
                       map(eval,
                           map(lambda s: s.replace('/', '//'),
                               takewhile(lambda s: '?' not in s,
                                         iter(input, ''))))))