X = int(input())
c = 1
for i in [1799,1599,1399,1199,999,799,599,399]:
    if X > i :
        break
    c = c + 1
print(c)    