#   ?????????????????°???????????????????¨??????????????????°??????
while 1:
    #   ?¨??????\???????????°???????????????
    input_num = list(input())
    #   ???????????????"0"??\?????§??????
    if int(input_num[0]) == 0:
        break
    #   print(input_num)
    #   ??????????¨?????????????????????°
    digitTotal = 0
    for i in range(0, len(input_num)):
        digitTotal += int(input_num[i])
    print("{0}".format(digitTotal))