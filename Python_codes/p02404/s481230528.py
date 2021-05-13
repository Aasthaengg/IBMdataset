'''
ITP-1_5-B
 ?????¬???????????????
??\????????????????????????H cm ?????? W cm ???????????????????????°?????????????????????????????????
##########
#........#
#........#
#........#
#........#
##########
?????????????????? 6 cm ?????? 10 cm ???????????¨??????????????????
???Input
??\???????????°????????????????????????????§???????????????????????????????????????????????????¢????????\????????¨????????§??????
H W
H, W ?????¨?????? 0 ?????¨????????\?????????????????¨????????????
???Output
?????????????????????????????????????????? H cm ?????? W cm ?????????????????????????????????
?????????????????????????????????????????????????????\??????????????????
'''
# import
import sys

for line in sys.stdin:
    # ?????°??????????????????
    H, W = map(int, line.split())
    if H == 0 and W == 0:
        break
    # ?????¢??????
    print('#' * W)
    for a in range(H-2):
        print('#'+'.'*(W-2)+'#')
    print('#' * W)
    print('')