# -*- coding: utf-8 -*-
a, b, c, d = map(int, input().split())
ac = abs(a-c) <= d
ab = abs(a-b) <= d
bc = abs(b-c) <= d
print(['No', 'Yes'][ac or (ab and bc)])