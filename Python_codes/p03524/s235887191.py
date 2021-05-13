#!/usr/bin/env python3
s = input()
abc_cnt = [s.count("a"),s.count("b"),s.count("c")]
if max(abc_cnt) - min(abc_cnt) > 1:
    print("NO")
else:
    print("YES")