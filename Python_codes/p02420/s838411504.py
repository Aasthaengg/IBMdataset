while True:
    str=input()
    tmp=str
    if str == '-':
        break
    times=int(input())
    for i in range(times):
        lth=int(input())
        tmp=str[0:lth]
        str=str[lth::]+tmp
    print(str)
