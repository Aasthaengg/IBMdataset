#!/usr/bin/env python3

import re
S = input()
S = re.sub("W+", "W", S)
S = re.sub("B+", "B", S)
print(len(S) - 1)