from itertools import product
(lambda *_: None)(
    *(lambda full, hand: map(print,
                             filter(lambda c: c not in hand, full)))(
        map(' '.join, product('SHCD', map(str, range(1, 14)))),
        set(map(lambda _: input(), range(int(input()))))))