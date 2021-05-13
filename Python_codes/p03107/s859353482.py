s = input()

if len(s)>0:
    print(min(s.count("0"),s.count("1"))*2)