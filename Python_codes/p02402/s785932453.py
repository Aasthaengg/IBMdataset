'''
ITP-1_4-D
 ????°????????????§??????????¨????
n????????´??° ai(i=1,2,...n)ai(i=1,2,...n)?????\?????????????????????????°????????????§??????????¨????????±???????????????°????????????????????????????????????
???Input
??????????????´??°?????° nn ???????????????????????????????????? nn ????????´??° aiai ????????????????????§?????????????????????
???Output
????°????????????§??????????¨????????????????????????§????????????????????????????????????
'''
# import
import sys

# ?????°??????????????????
n = int(input())
inputData = map(int, input().split())
maxData = -1000000
minData = 1000000
totalData = 0

for inputVal in inputData:

    # max value check
    if inputVal > maxData:
        maxData = inputVal

    # minimum value check
    if inputVal < minData:
        minData = inputVal

    # total value add
    totalData += inputVal

# ????????????
print(minData, maxData, totalData)