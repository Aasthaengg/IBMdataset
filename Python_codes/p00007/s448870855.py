from __future__ import (division, absolute_import, print_function,
                        unicode_literals)
debt = 100000.0
for i in xrange(int(raw_input())):
    debt += debt * 0.05
    debt = debt - (debt % 1000.0) + (1000.0 if debt % 1000.0 else 0.0)
print(int(debt))