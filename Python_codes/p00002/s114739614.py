# coding: utf-8

import codecs
import sys

sys.stdout = codecs.getwriter("shift_jis")(sys.stdout) # ??????
sys.stdin = codecs.getreader("shift_jis")(sys.stdin) # ??\???

# ??\??¬?????????print??????????????´?????? print(u'?????????') ??¨??????
# ??\??¬?????????input??? input(u'?????????') ??§OK
# ??°?¢???????????????????????????´??????6,7???????????????????????¢??????

"""
DEBUG = 0

if DEBUG == 0:
	a = []
	for i in range(200):
		deglist=[int(x) for x in input().split(" ")]
		a.append(deglist)
else:
	a = [[5,7],[1,99],[1000,999]]

for i in range(len(a)):
	wa = a[i][0] + a[i][1]
	print len(str(wa))
"""

while True:
	try:
		a,b = map(int, raw_input().split())
		print len(str(a+b))
	except EOFError:
		break