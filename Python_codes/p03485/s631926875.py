a, b = map(int, input().split())
ave=(a+b)/2
if ave-int(ave)==0:
    print(int(ave))
else:
    print(int(ave)+1)
