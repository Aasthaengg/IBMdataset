'''
ITP-1_10-A
 ?????¢
?????? P1(x1, y1), P2(x2, y2) ????????¢????±???????????????°????????????????????????
???Input
x1, y1, x2, y2 ????????°???????????????????????§?????????????????????
???Output
P1??¨P2????????¢????????°??§?????????????????????????????????0.0001??\????????????????????£????????????????????¨????????????
'''
# # import
# import numpy
# 
# # inputData
# Data = input().split()
# x1 = int(Data[0])
# y1 = int(Data[1])
# x2 = int(Data[2])
# y2 = int(Data[3])
# 
# P1 = numpy.array([x1, y1])
# P2 = numpy.array([x2, y2])
# print(numpy.linalg.norm(P2 - P1))

import math

def get_distance(x1, y1, x2, y2):
    d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return d

if __name__ == '__main__':
    # inputData
    Data = input().split()
    x1 = float(Data[0])
    y1 = float(Data[1])
    x2 = float(Data[2])
    y2 = float(Data[3])

    d = get_distance(x1, y1, x2, y2)
    print(d)