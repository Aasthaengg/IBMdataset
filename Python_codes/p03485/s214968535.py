a, b = map(int, input().split())
ave = (a+b)/2
cuted_ave = (a+b)//2
if ave == cuted_ave:
    print(int(ave))
else:
    print(int(cuted_ave+1))