#!/usr/bin/env python3
import re

s = input()
s = "".join(s.split("eraser"))
s = "".join(s.split("erase"))
s = "".join(s.split("dreamer"))
s = "".join(s.split("dream"))

print("YES" if s == "" else "NO")
