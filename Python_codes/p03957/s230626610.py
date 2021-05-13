#!/usr/bin/env python3

import re
s = input()
m = re.findall(r"C.*F", s)
print("Yes") if m else print("No")
