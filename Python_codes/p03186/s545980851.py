# -*- coding: utf-8 -*-
nontastyDetox, tastyDedox, tastyToxic = map(int, input().split())

if nontastyDetox + tastyDedox + 1 >= tastyToxic:
	print(tastyDedox + tastyToxic)
else:
	print(nontastyDetox + 2 * tastyDedox + 1)
