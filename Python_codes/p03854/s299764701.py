#!/usr/bin/env python3
import re
s = input()
s = re.sub(r'erase(r|)',"", s)
s = re.sub(r'dream(er|)',"", s)
print('YNEOS'[s!=""::2])
