#   1???????????? W ??¨?????? T ,T ??????????????? W ?????°???????????????????????°??????
import sys
#   ??????W?????????
w = input()
#   ??????T?????????
t = []
#   ??????T?????????
while 1:
    temp = input()
    if temp == "END_OF_TEXT":
        break
    t += temp.strip(".")
    t += " "
#   ??????????????????
t = "".join(t).split()
#   print(t)
#   ??????T???????????¨????????????W????????????????????????
count = 0
for i in range(len(t)):
    if t[i].lower() == w:
        count += 1
print(count)