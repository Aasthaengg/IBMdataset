# 19-String-Finding_a_Word.py

# ?????????????´¢
# ??????????????? W ??¨?????? T ????????????????????????T ??????????????? W ?????°???????????????????????°?????????????????????????????????
# ?????? T ????????????????????????????????????????????§????????????????????????????????? Ti ??¨????????????
# ???????????? Ti ?????????????????? W ??¨??????????????????????????°??????????????????
# ???????????§????????¨?°???????????????\???????????????

# Constraints
# W????????????????????????10????¶????????????????
# T??????????????????????????????????????????1000????¶????????????????

# Input
# ?????????????????? W ????????????????????????
# ?¶???????????????°????????????????????£??????????????????????????????
# END_OF_TEXT ??¨??????????????????????????????????????????????????????

# Output
# ?????? W ?????°???????????????????????????

# Sample Input
# computer
# Nurtures computer scientists and highly-skilled computer engineers
# who will create and exploit "knowledge" for the new era.
# Provides an outstanding computer environment.
# END_OF_TEXT

# Sample Output
# 3
# Note

import re

count=0

w = input().lower()

while 1:
	string = input()
	if string=="END_OF_TEXT":
		break;

	for i in string.lower().split():
		count += w==i

print(count)