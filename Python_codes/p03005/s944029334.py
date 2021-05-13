# -*- coding: utf-8 -*-
import sys
N, M= map(int, raw_input().split())
if M == 1:
	result = 0
else:
	result = N-M
print result