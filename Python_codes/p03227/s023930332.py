_str=input()
if(len(_str)==2):
    print(_str)
else:
    for i in range(2,-1,-1):
        print(_str[i],end="")
    print()