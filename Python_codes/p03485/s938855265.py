a,b = map(int,input().split())
ave = (a+b)/float(2)
if ave == int(ave):
    print(int(ave))
elif ave > int(ave):
    print(int(ave)+1)