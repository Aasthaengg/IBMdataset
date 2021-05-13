s = input()
count1 = s.count("1")
count0 = s.count("0")
if count0 == count1 :
    print(len(s))
else :
    print(min(count1, count0)*2)
