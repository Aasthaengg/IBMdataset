# 18-Character-Ring.py

# ????????°
# ???????????????????????°??¶???????????? s ???????????????????????????????¨????????????£?¶????????????????????????????????????§???
# ????????? p ??????????????????????????????????????°????????????????????????????????????

# Input
# ????????????????????? s ????????????????????????
# ????????????????????? p ????????????????????????

# Output
# p ??????????????´?????? Yes ??¨?????????????????´?????? No ??¨????????????????????????????????????

# Constraints
# 1???p????????????s????????????100
# ??????????????±?°???????????????????

# Sample Input 1
# vanceknowledgetoad
# advance
# Sample Output 1
# Yes

# Sample Input 2
# vanceknowledgetoad
# advanced
# Sample Output 2
# No

import re

pattern=[]

s=input()
p=input()

s= s+s

# for p2 in list(p):
# 	pattern.append(p2)
# 	pattern.append(".*")

# pattern = "".join(pattern)
# print(pattern)

matchOB = re.search(p, s)

if matchOB:
	print("Yes")
else:
	print("No")