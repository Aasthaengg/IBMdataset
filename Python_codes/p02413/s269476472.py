'''
ITP-1_7-C
 ??¨?¨????
??¨?¨??????????????°???????????????°???????????????????????????
??¨????????°r??¨?????°c???r ?? c ???????´????????????¨?????????????????§???????????¨??????????¨?????????\????????°????????¨???????????????
????????°?????????????????????????????????
???Input
???????????????r??¨c????????????????????§??????????????????????¶????r??????????????????c????????´??°????????????????????§?????????????????????
???Output
(r+1) ?? (c+1) ?????°????????¨??????????????????????????????????????£???????????´??°????????????????????§????????£???????????????
???????????????????????¨??????????????????????¨?????????????????????????????????¨??????????????????????¨??????????
???????????????????????¨??¨??????????¨????????????\??????????????????
'''
# inputData
r, c = map(int, input().split())
data = [list(map(int, input().split())) for i in range(r)]

for row in data:
    row.append(sum(row))
    print(*row)

# zip ????´?????????????????????????????????¨?????§????????????????????§??????
columnSum = [sum(Column) for Column in zip(*data)]
print(*columnSum)