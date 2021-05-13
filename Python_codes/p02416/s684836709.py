while True :
    tem = input()
    res = 0
    if tem == '0' : break
    for i in tem : res += int(i)
    print(res)